word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if len(word1) != len(word2):
    print(False)
else:
    letters1 = list(word1)
    letters2 = list(word2)

    letters1.sort()
    letters2.sort()

    if letters1 == letters2:
        print(True)
    else:
        print(False)

