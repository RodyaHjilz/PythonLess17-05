def foldl(func, lst, acc):
    for element in lst:
        acc = func(acc, element)
    return acc


def add(x, y):
    return x + y


lst = [1, 2, 3, 4, 5]
acc = 0

result = foldl(add, lst, acc)
print(result)
