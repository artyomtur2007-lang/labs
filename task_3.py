password = input("Введите пароль: ")

if len(password) < 16:
    print("Слишком короткий")
else:
    only_b = True
    only_c = True
    for el in password:
        if not el.isalpha():
            only_b = False
        if not el.isdigit():
            only_c = False

    if only_b or only_c:
        print("Слабый пароль")
    else:
        print("Надежный пароль")
