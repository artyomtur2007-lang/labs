def unique_elements(lst):
    unique_list = []
    def flatten(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                flatten(item)
            else:
                if item not in unique_list:
                    unique_list.append(item)

    flatten(lst)
    return unique_list

def merge_sorted_list(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_list(list1, list2)
print(f"Объединенный отсортированный список: {merged_list}")

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9,2,3]]]]
print(f"Уникальные элементы списка list_a: {unique_elements(list_a)}")
