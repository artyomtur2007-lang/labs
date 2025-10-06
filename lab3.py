class bank:
    def __init__(self,name):
        self.name=name
        self.accounts={}
        self.client={}
    def add_clients(self,client):
         self.client=client
    def open_account(self,client,currency):
        #если нет аккаунта то класс исключения,если уже есть валюта тоже
    def close_account(self,):
class account:
    def __init__(self,client,currency):
        self.currency=currency
        self.client=client
        # self.account_id
        # def deposit(self, amount):
class client:
    def __init__(self, name,clients_id=None):
        self.name=name
        #self.clients_id=
        self.accounts={}
    def __str__(self):
