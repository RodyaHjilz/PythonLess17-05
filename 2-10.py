def foldr(func, lst, acc):
    for element in reversed(lst):
        acc = func(element, acc)
    return acc


def add(x, y):
    return x + y


lst = [1, 2, 3, 4, 5]
acc = 0

result = foldr(add, lst, acc)
print(result)
