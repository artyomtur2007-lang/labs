import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Угадайте число от 1 до 100: "))

    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print("Поздравляю, вы угадали! Это число", secret_number)

