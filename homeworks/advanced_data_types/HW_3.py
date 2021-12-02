# 1Task
int_a = 55
print(id(int_a))
str_b = 'Cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

# 2Task
lst_d = [1, 2, 3]
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# 3Task
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4Task
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#   5Task
print("Anna has {} apples and {} peaches.".format(4, 5))
#   6Task
print("Anna has {0} apples and {1} peaches.".format("four", "five"))
#   7Task
print("Anna has {0} apples and {fv} peaches.".format("four", fv="five"))
# 8Task
print("Anna has {0:5} apples and {1:3} peaches.".format("four", "five"))
# 9Task
apple = 8
peache = 4
print(f"Anna has {apple} apples and {peache} peaches.")
# 10task
app = 9
peac = 6
print("Anna has %d apples and %d peaches" % (app, peac))
# 11Task
app = 10
peac = 4
dict = {"apple": app, "peaches": peac}
print("Anna has %(apple)d apples and %(peaches)d peaches" % dict)

# 12task
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
# 13 task
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# 14task
dict_comprehension = {d: d ** 2 for d in range(1, 11) if d % 2 == 1}
print(dict_comprehension)

# 15task
dict_comprehension = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range(1, 11)}
print(dict_comprehension)

# 16 task
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
print(x)

# 17 task
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
    else:
        x[num] = num
print(x)

# 18 task
foo = lambda x, y: x if x < y else y
print(foo(2, 3))


# 19 task
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(5, 6, 8))

# 20 task
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21task
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))

# 22 task
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort)

# 23 task
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_3 = list(map(lambda x, y: x + y, list_A, list_B))
print(list_3)

# 24task
import functools

lst_to_sort_ = lambda x, y: x + y
lst_to_sort_2 = functools.reduce(lst_to_sort_, lst_to_sort)
print(lst_to_sort_2)

# 25task
lst_filter = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_filter)

# 26 task
lst_minus = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_minus)

# 27 task
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
new_list = list(filter(lambda x: x in list_1, list_2))
print(new_list)
