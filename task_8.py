import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"Время выполнения функции {func.__name__}: {execution_time_ms:.2f} мс")
        return result

    return wrapper


@timing
def my_function(n):
    time.sleep(n)
    return f"Функция my_function завершена после {n} секунд ожидания."


print("Вызываем функцию my_function(2):")
result = my_function(2)
print(f"Результат выполнения: {result}")

print("\nВызываем функцию my_function(0.5):")
result = my_function(0.5)
print(f"Результат выполнения: {result}")


