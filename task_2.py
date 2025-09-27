str= input("Введите строку: ")
newstr= ""
glas= "aeiouAEIOU"
for i in str:
    if i not in glas:
        newstr = newstr + i
print("Строка без гласных:", newstr)

