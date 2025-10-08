day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения (числом): "))

if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Козерог")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Водолей")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Рыбы")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Овен")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Телец")
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("Близнецы")
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("Рак")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Лев")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Дева")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Весы")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Скорпион")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Стрелец")
else:
    print("Неверный ввод")

