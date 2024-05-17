def list_replace(lst, index, value):
    if index < 0 or index >= len(lst):
        raise IndexError("Ошибка индекса")
    lst[index] = value
    return lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_replace(my_list, 3, 15)
print(my_list)

list_replace(my_list, 10, 10)