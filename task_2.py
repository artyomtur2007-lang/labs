input_str = input("Введите числа через пробел: ")
str_list = input_str.split()
num_list = []

for s in str_list:
    num = float(s)
    num_list.append(num)

# Уникальные числа
unique_nums = []
for num in num_list:
    if num not in unique_nums:
        unique_nums.append(num)
print("Уникальные числа:", unique_nums)

# Повторяющиеся числа
repeated_nums = []
for num in num_list:
    count = 0
    for other_num in num_list:
        if num == other_num:
            count += 1
    if count > 1 and num not in repeated_nums:
        repeated_nums.append(num)
print("Повторяющиеся числа:", repeated_nums)

# Четные и нечетные числа
even_nums = []
odd_nums = []
for num in num_list:
    if num == int(num):
        if int(num) % 2 == 0:
            even_nums.append(int(num))
        else:
            odd_nums.append(int(num))

print("Четные числа:", even_nums)
print("Нечетные числа:", odd_nums)

# Отрицательные числа
neg_nums = []
for num in num_list:
    if num < 0:
        neg_nums.append(num)
print("Отрицательные числа:", neg_nums)

# Числа с плавающей точкой
float_nums = []
for num in num_list:
    if num != int(num):
        float_nums.append(num)
print("Числа с плавающей точкой:", float_nums)

# Сумма чисел, кратных 5
sum_mult_5 = 0
for num in num_list:
    if num % 5 == 0:
        sum_mult_5 = sum_mult_5 + num
print("Сумма чисел, кратных 5:", sum_mult_5)

# Самое большое число
if num_list:
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    print("Самое большое число:", max_num)
else:
    print("Список чисел пуст, невозможно найти максимальное число.")

# Самое маленькое число
if num_list:
    min_num = num_list[0]
    for num in num_list:
        if num < min_num:
            min_num = num
    print("Самое маленькое число:", min_num)
else:
    print("Список чисел пуст, невозможно найти минимальное число.")



