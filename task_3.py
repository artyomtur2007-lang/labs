import time

def log_calls(filename):
  def decorator(func):
    def wrapper(*args, **kwargs):
      now = time.strftime("%Y-%m-%d %H:%M:%S")
      func_name = func.__name__
      arguments = str(args) + str(kwargs)
      log_string = f"{now} - {func_name} - Args: {arguments}\n"

      try:
        with open(filename, "a") as file:
          file.write(log_string)
      except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

      return func(*args, **kwargs)

    return wrapper
  return decorator

@log_calls("function_calls.log")
def my_function(a, b=10):
  return a + b

@log_calls("function_calls.log")
def another_function(name, age):
    print(f"Hello, {name}! You are {age} years old.")


result = my_function(5)
print(f"Результат my_function: {result}")

my_function(2, b=5)
another_function("Alice", 30)
