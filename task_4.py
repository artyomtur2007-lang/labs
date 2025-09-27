inp1 = input("Введите числа для первого набора через пробел: ")
lst1 = inp1.split()
nums1 = []
for s in lst1:
    num = float(s)
    nums1.append(num)

inp2 = input("Введите числа для второго набора через пробел: ")
lst2 = inp2.split()
nums2 = []
for s in lst2:
    num = float(s)
    nums2.append(num)

# 1. Числа, которые присутствуют в обоих наборах одновременно
common = []
for num1 in nums1:
    if num1 in nums2 and num1 not in common:
        common.append(num1)
print("1. Числа, присутствующие в обоих наборах:", common)

# 2. Числа из первого набора, которые отсутствуют во втором, и наоборот.
only1 = []
for num1 in nums1:
    if num1 not in nums2:
        only1.append(num1)
print("2. Числа только из первого набора:", only1)

only2 = []
for num2 in nums2:
    if num2 not in nums1:
        only2.append(num2)
print("2. Числа только из второго набора:", only2)

#  3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1.
unique = []
for num in only1:
    unique.append(num)
for num in only2:
    unique.append(num)
print("3. Числа, уникальные для каждого набора (исключая общие):", unique)


