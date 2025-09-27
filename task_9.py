ip = input("Введите IP-адрес: ")

nums = ip.split(".")

if len(nums) != 4:
    print("Некорректный IP-адрес (неверное количество частей).")
else:
    valid = True
    for num_str in nums:
        if not num_str.isdigit():
            valid = False
            break
        num = int(num_str)
        if num < 0 or num > 255:
            valid = False
            break

    if valid:
        print("Корректный IP-адрес.")
    else:
        print("Некорректный IP-адрес (неверный формат чисел).")
