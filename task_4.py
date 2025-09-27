amount = int(input(" Введите количество рублей: "))

hundreds = amount // 100
amount = amount % 100

fifties = amount // 50
amount = amount % 50

tens = amount // 10
amount = amount % 10

fives = amount // 5
amount = amount % 5

twos = amount // 2
amount = amount % 2

ones = amount

print("Hundreds:", hundreds)
print("Fifties:", fifties)
print("Tens:", tens)
print("Fives:", fives)
print("Twos:", twos)
print("Ones:", ones)
