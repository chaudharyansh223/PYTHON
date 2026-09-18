list_a = [10, 20, 30, 40, 50]
list_b = [20, 30, 60, 70]
list_c = [30, 20, 80, 90]

set_a = set(list_a)
result  = 0
result = set_a.intersection(list_b,list_c)
print(list(result))