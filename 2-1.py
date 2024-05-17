def pair(head, tail):
  return [head] + tail

def head(lst):
  return lst[0]

def tail(lst):
  return lst[1:]

my_list = pair(1, [2, 3, 4])
print(my_list)

head_value = head(my_list)
print(head_value)

tail_list = tail(my_list)
print(tail_list)