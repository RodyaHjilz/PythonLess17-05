def add(x, y):
    return x + y


def foldl(func, lst, acc):
    for element in lst:
        acc = func(acc, element)
    return acc


def list_sum(lst):
    return foldl(add, lst, 0)


my_list = [1, 2, 3, 4, 5]
result = list_sum(my_list)
print(result)
