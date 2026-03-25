from copy import deepcopy

list1 = [32, 43, 54, [111, 222, 333], 65, 67, 76, 63]

# list2 = list1.copy()  # Shallow Copy
list2 = deepcopy(list1)  # Deep Copy
print(id(list1))
print(id(list2))
print("-------")
print(id(list1[3]))
print(id(list2[3]))

list1[3][2] = 1000


print(f"list1 = {list1}")
print(f"list2 = {list2}")
