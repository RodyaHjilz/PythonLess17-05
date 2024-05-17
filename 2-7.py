def foldl(func, lst, acc):
    for element in lst:
        acc = func(acc, element)
    return acc


def list_range(n):
    return list(range(1, n + 1))

def prepend(acc, x):
    return acc*x
def fact(n):
    if n == 0:
        return 1
    else:
        return foldl(prepend, list_range(n), 1)


print(fact(5))
