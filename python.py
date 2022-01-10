def countdown(new_list, num):
  for x in range(num):
    new_list.append(num-x)
  num = num-1
  return new_list
b = countdown([], 5)
print(b)

# funciton played(list, num) {
#   for(var i=0; i<list; i--) {
#     list.append(num-i)
#     if num-i>list.length;
#   }
# }
# played([],)

def print_return(list):
  print(list[0])
  return list[1]
b = print_return([1,2])
print(b)

def length_of(list):
  sum = list[0] + len(list)
  return sum
length_add=length_of([1,2,3,4,5])
print(length_add)

def value_greater(list):
  new_list = []

  for x in range(len(list)):
    if len(list) < 2:
      return False
    else:
      if list[x] > list[1]:
        new_list.append(list[x])
  print(len(new_list))
  return new_list
val = value_greater([5,2,3,2,1,4])
print(val)

def length_value(size, val):
  list = []

  for x in range(size):
    list.append(val)
  return list
len = length_value(6,2)
print(len)