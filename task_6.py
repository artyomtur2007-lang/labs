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

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9,2,3]]]]
print(unique_elements(list_a))
