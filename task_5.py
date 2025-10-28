number = int(input("Введите число: "))
number_str = str(number)
digit_sum = 0
for digit in number_str:
  digit_sum += int(digit)

if number % 7 == 0:
  print("Магическое число!")
else:
  print(digit_sum)
