def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Берем результат из кэша")
            return cache_dict[key]
        else:
            print("Вычисляем результат функции")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


@cache
def my_function(a, b=1):
    print("Функция вызвана")
    return a + b

@cache
def another_function(x, y):
    print("Другая функция вызвана")
    return x * y

print("Первый вызов my_function(2):", my_function(2))
print("Второй вызов my_function(2):", my_function(2))
print("Третий вызов my_function(2, b=3):", my_function(2, b=3))
print("Четвертый вызов my_function(2, b=3):", my_function(2, b=3))
print("Вызов another_function(3,4)", another_function(3,4))
print("Вызов another_function(3,4)", another_function(3,4))
