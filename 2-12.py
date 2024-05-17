def foldr(func, lst, acc):
  for element in reversed(lst):
    acc = func(element, acc)
  return acc

def filter_item(x, acc, pred):
  if pred(x):
    return [x] + acc
  else:
    return acc

def list_filter(pred, lst):
  def inner_func(x, acc):
    return filter_item(x, acc, pred)
  return foldr(inner_func, lst, [])

def greater(x):
  return x >= 5

lst = [1, 2, 3, 4, 5, 6]
print(list_filter(greater, lst))