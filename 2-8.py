def foldl(func, lst, acc):
  for element in lst:
    acc = func(acc, element)
  return acc

def prepend(acc, x):
    return acc + [x]
def list_to_py(lst):
  return foldl(prepend, lst, [])

my_list = [1, 2, 3, 4, 5]
python_list = list_to_py(my_list)
print(python_list)