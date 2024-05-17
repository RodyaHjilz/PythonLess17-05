def foldr(func, lst, acc):
    for element in reversed(lst):
        acc = func(element, acc)
    return acc


def map_item(x, acc, func):
    return [func(x)] + acc


def list_map(func, lst):
    def inner_func(x, acc):
        return map_item(x, acc, func)

    return foldr(inner_func, lst, [])


def square(x):
    return x * x


lst = [1, 2, 3, 4, 5]
print(list_map(square, lst))
