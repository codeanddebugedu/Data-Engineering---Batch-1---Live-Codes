def func(x):
    return x[2]


my_list = [[1, 2, 333], [54, 453, 2], [6, 76, 331], [78, 65, 35]]
my_list.sort(key=lambda x: x[2])
# my_list.sort(key=func)
print(my_list)


# x = sorted(my_list)
# print(x)
# print(my_list)
