f = input("Введите фамилию: ")
i = input("Введите имя: ")
o = input("Введите отчество: ")
firstf=f.capitalize()
firsti= i[0].upper()
firsto = o[0].upper()
result = firstf+' '+firsti+'.'+firsto+'.'
print('ФИО',result)
