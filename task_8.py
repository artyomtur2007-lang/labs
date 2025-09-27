text = input("Введите строку: ")
ntext = text.lower().replace(" ", "")
revertext = ntext[::-1]

if ntext == revertext:
    print("Это палиндром!")
else:
    print("Это не палиндром.")
