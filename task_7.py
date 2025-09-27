inp_str = input("Введите строку: ")
result_str = ""
count = 1

for i in range(len(inp_str)):
    if i + 1 < len(inp_str) and inp_str[i] == inp_str[i+1]:
        count += 1
    else:
        result_str += inp_str[i] + str(count)
        count = 1

print(result_str)

