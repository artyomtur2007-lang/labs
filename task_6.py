inp = input("Введите список элементов через пробел: ")
lst = inp.split()
unique = []

for elem in lst:
    if elem not in unique:
        unique.append(elem)

print("Список без дубликатов:", unique)

