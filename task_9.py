def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"Неверное количество аргументов: ожидалось {len(expected_types)}, получено {len(args)}"
                )

            for i, arg in enumerate(args):
                expected_type = expected_types[i]
                if type(arg) != expected_type:
                    raise TypeError(
                        f"Аргумент {i + 1} имеет неверный тип: ожидался {expected_type}, получен {type(arg)}"
                    )

            result = func(*args)
            return result

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


@type_check(str, int, float)
def describe_person(name, age, height):
    return f"Имя: {name}, Возраст: {age}, Рост: {height}"


print(f"Результат add(5, 3): {add(5, 3)}")
print(f"Результат describe_person('Alice', 30, 1.65): {describe_person('Alice', 30, 1.65)}")


try:
    add(5, "3")
except TypeError as e:
    print(f"Ошибка в add(5, '3'): {e}")

try:
    describe_person("Bob", 25, "1.75")
except TypeError as e:
    print(f"Ошибка в describe_person('Bob', 25, '1.75'): {e}")

try:
    add(1, 2, 3)
except TypeError as e:
    print(f"Ошибка в add(1, 2, 3): {e}")

