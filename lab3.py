
import datetime

class InsufficientFundsError(Exception):
    """Исключение, выбрасываемое при попытке снять больше средств, чем есть на счете."""
    pass

class AccountNotFoundError(Exception):
    """Исключение, выбрасываемое, если счет не найден."""
    pass

class ClientAlreadyHasAccountInCurrencyError(Exception):
    """Исключение, если клиент пытается открыть счет в валюте, в которой у него уже есть счет."""
    pass

class InvalidAmountError(Exception):
    """Исключение, если сумма для пополнения/снятия/перевода не является положительным числом."""
    pass

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}
        self.accounts = {}
        self.next_client_id = 1000
        self.next_account_id = 2000
        self.exchange_rates = {
            "EUR": 3.5,  # EUR = 3.5 BUN
            "USD": 3.0,  # USD = 3.0 BUN
            "BUN": 1.0,  # BUN = 1.0 BUN
        }
        self.currency_relations = {
            ("USD", "EUR"): 0.85, # USD = 0.85 EUR
            ("EUR", "USD"): 1.18, # EUR = 1.18 USD
        }

    def generate_client_id(self):
        client_id = str(self.next_client_id)
        self.next_client_id += 1
        return client_id

    def generate_account_id(self):
        account_id = str(self.next_account_id)
        self.next_account_id += 1
        return account_id

    def create_client(self, name, address):
        client_id = self.generate_client_id()
        client = Client(client_id, name, address)
        self.clients[client.client_id] = client
        return client

    def open_account(self, client_id, currency):
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Клиент не найден.")

        if client.has_account_in_currency(currency):
            raise ClientAlreadyHasAccountInCurrencyError("У клиента уже есть счет в этой валюте.")

        account_id = self.generate_account_id()
        account = BankAccount(account_id, client_id, currency)
        self.accounts[account.account_id] = account
        client.accounts[currency] = account.account_id
        return account

    def close_account(self, account_id, client_id):
        account = self.accounts.get(account_id)
        if not account:
            raise AccountNotFoundError("Счет не найден.")

        if account.client_id != client_id:
            raise ValueError("Клиент не является владельцем этого счета.")

        client = self.clients[client_id]
        for currency, acc_id in client.accounts.items():
            if acc_id == account_id:
                del client.accounts[currency]
                break

        del self.accounts[account_id]

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def deposit(self, account_id, amount):
        account = self.accounts.get(account_id)
        if not account:
            raise AccountNotFoundError("Счет не найден.")

        if amount <= 0:
            raise InvalidAmountError("Сумма должна быть положительной.")

        account.deposit(amount)

    def withdraw(self, account_id, amount):
        account = self.accounts.get(account_id)
        if not account:
            raise AccountNotFoundError("Счет не найден.")

        if amount <= 0:
            raise InvalidAmountError("Сумма должна быть положительной.")

        account.withdraw(amount)

    def convert_currency(self, amount, from_currency, to_currency):
        """Конвертирует валюту, используя заданные курсы."""
        if from_currency == to_currency:
            return amount

        if from_currency == 'BUN':
            bun_amount = amount
        else:
            bun_amount = amount * self.exchange_rates[from_currency]

        if to_currency == 'BUN':
            return bun_amount
        else:
            converted_amount = bun_amount / self.exchange_rates[to_currency]
            return converted_amount

    def transfer(self, from_account_id, to_account_id, amount):
        from_account = self.accounts.get(from_account_id)
        to_account = self.accounts.get(to_account_id)

        if not from_account or not to_account:
            raise AccountNotFoundError("Один или оба счета не найдены.")

        if amount <= 0:
            raise InvalidAmountError("Сумма должна быть положительной.")

        from_currency = from_account.currency
        to_currency = to_account.currency

        try:
            from_account.withdraw(amount)

            if from_currency != to_currency:
                # Конвертируем сумму при разных валютахх
                converted_amount = self.convert_currency(amount, from_currency, to_currency)
                to_account.deposit(converted_amount)
                print(f"Переведено {amount} {from_currency} -> {converted_amount} {to_currency}")

            else:
                to_account.deposit(amount)
                print(f"Переведено {amount} {from_currency} to {to_currency}")

        except InsufficientFundsError:
            print(f"Недостаточно средств на счете {from_account_id} для перевода {amount} {from_currency}")
            from_account.deposit(amount)
            raise

    def get_client_accounts(self, client_id):
        client = self.clients.get(client_id)
        if not client:
            return []
        return [self.accounts[account_id] for account_id in client.accounts.values()]

    def generate_statement(self, client_id, filename="statement.txt"):
        client = self.clients.get(client_id)
        if not client:
            print("Клиент не найден.")
            return

        accounts = self.get_client_accounts(client_id)
        if not accounts:
            print("У этого клиента нет счетов.")
            return

        total_balance = 0
        with open(filename, "w") as f:
            f.write(f"Выписка для клиента ID: {client_id}\n")
            f.write(f"Имя клиента: {client.name}\n")
            f.write(f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("----------------------------------------\n")
            for account in accounts:
                f.write(f"ID счета: {account.account_id}\n")
                f.write(f"Валюта: {account.currency}\n")
                f.write(f"Баланс: {account.balance}\n")
                f.write("----------------------------------------\n")
                total_balance += account.balance

            f.write(f"Общий баланс по всем счетам: {total_balance}\n")
        print(f"Выписка создана и сохранена в файл: {filename}")


class Client:
    def __init__(self, client_id, name, address):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.accounts = {}

    def has_account_in_currency(self, currency):
        return currency in self.accounts


class BankAccount:
    def __init__(self, account_id, client_id, currency, balance=0.0):
        self.account_id = account_id
        self.client_id = client_id
        self.currency = currency
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Внесено {amount} {self.currency}. Новый баланс: {self.balance} {self.currency}")

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError("Недостаточно средств на счете.")
        self.balance -= amount
        print(f"Снято {amount} {self.currency}. Новый баланс: {self.balance} {self.currency}")

def main():
    bank = Bank("MyBank")

    while True:
        print("\n--- Банковское меню ---")
        print("1. Создать клиента")
        print("2. Войти по ID клиента")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя клиента: ")
            address = input("Введите адрес клиента: ")
            client = bank.create_client(name, address)
            print(f"Клиент создан с ID: {client.client_id}")

        elif choice == "2":
            client_id = input("Введите ID клиента: ")
            if client_id not in bank.clients:
                print("Неверный ID клиента.")
                continue

            client_menu(bank, client_id)

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def client_menu(bank, client_id):
    while True:
        print("\n--- Меню клиента ---")
        print("1. Открыть счет")
        print("2. Закрыть счет")
        print("3. Пополнить счет")
        print("4. Снять со счета")
        print("5. Перевести деньги")
        print("6. Сформировать выписку")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            currency = input("Введите валюту для нового счета (например, USD, EUR, RUB): ")
            try:
                account = bank.open_account(client_id, currency)
                print(f"Счет создан с ID: {account.account_id}")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except ClientAlreadyHasAccountInCurrencyError as e:
                 print(f"Ошибка: {e}")

        elif choice == "2":
            account_id = input("Введите ID счета для закрытия: ")
            try:
                bank.close_account(account_id, client_id)
                print("Счет успешно закрыт.")
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            account_id = input("Введите ID счета для пополнения: ")
            amount = float(input("Введите сумму для пополнения: "))
            try:
                bank.deposit(account_id, amount)
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except InvalidAmountError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            account_id = input("Введите ID счета для снятия средств: ")
            amount = float(input("Введите сумму для снятия: "))
            try:
                bank.withdraw(account_id, amount)
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except InsufficientFundsError as e:
                print(f"Ошибка: {e}")
            except InvalidAmountError as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            from_account_id = input("Введите ID счета-отправителя: ")
            to_account_id = input("Введите ID счета-получателя: ")
            amount = float(input("Введите сумму для перевода: "))
            try:
                bank.transfer(from_account_id, to_account_id, amount)
                print("Перевод успешно выполнен.")
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except InsufficientFundsError as e:
                print(f"Ошибка: {e}")
            except InvalidAmountError as e:
                print(f"Ошибка: {e}")

        elif choice == "6":
            filename = input("Введите имя файла для выписки (например, statement.txt): ")
            bank.generate_statement(client_id, filename)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
