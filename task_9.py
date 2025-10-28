ip=input('Введите IP-адрес:')
part=ip.split('.')
if len(part)!=4:
    print('Некорректный IP-адрес')
else:
    if (part[0].isdigit() and 0 <= int(part[0]) <= 255
        and part[1].isdigit() and 0<=int(part[1])<=255
        and part[2].isdigit() and 0<=int(part[2])<=255
        and part[3].isdigit() and 0<=int(part[3])<=255):
        print('Корректный IP-адрес')
    else:
        print('Некорректный IP-адрес')