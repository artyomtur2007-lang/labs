input_str = input("Введите числа через пробел: ")
str_list = input_str.split()
num_list = []

for s in str_list:
    num = float(s)
    num_list.append(num)

if len(num_list) < 2:
    print("Нужно ввести хотя бы два числа.")
else:
    unique_nums = []
    for n in num_list:
        if n not in unique_nums:
            unique_nums.append(n)

    if len(unique_nums) < 2:
        print("После удаления повторов осталось меньше двух чисел.")
    else:
        unique_nums.sort()
        second_largest = unique_nums[len(unique_nums) - 2]

        print("Второе по величине число:", second_largest)
