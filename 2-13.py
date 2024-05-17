def list_sum(lst):
    return sum(lst)


def list_map(func, lst):
    return [func(x) for x in lst]


def list_filter(pred, lst):
    return [x for x in lst if pred(x)]


def sum_odd_squares(lst):
    def is_odd(x):
        return x % 2 != 0

    def square(x):
        return x ** 2

    odd_numbers = list_filter(is_odd, lst)
    odd_squares = list_map(square, odd_numbers)
    return list_sum(odd_squares)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_odd_squares(my_list)
print(result)