def foldl(func, lst, acc):
    for element in lst:
        acc = func(acc, element)
    return acc


def prepend(acc, x):
    return [x] + acc


def list_reverse(lst):
    return foldl(prepend, lst, [])


my_list = [1, 2, 3, 4, 5]
reversed_list = list_reverse(my_list)
print(reversed_list)
