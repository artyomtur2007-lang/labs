def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            lst[i:i+1] = flatten_list(lst[i])
            i = 0
        else:
            i += 1
    return lst

list_a = [1, 2, 3, [4], 5, [6, [7, [8]]], 9]
print("Исходный список:", list_a)
flatten_list(list_a)
print("Модифицированный список:", list_a)



