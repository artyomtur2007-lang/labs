password = input("Введите пароль: ")

if len(password) < 16:
    print("Слишком короткий")
else:
    only_b =False
    only_c =False
    if password.isalpha():
            only_b = True
    if password.isdigit():
            only_c = True
    if only_b or only_c:
        print("Слабый пароль")
    else:
        print("Надежный пароль")
