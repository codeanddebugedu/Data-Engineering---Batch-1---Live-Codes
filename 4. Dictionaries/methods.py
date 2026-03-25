from copy import deepcopy

my_dict = {
    "name": "Anirudh",
    "age": 545,
    "gender": "Male",
    "ages": [432, 32, 13, 21321, 21],
}

diction2 = deepcopy(my_dict)

my_dict["ages"][0] = 1000

print(id(my_dict))
print(id(diction2))

# my_dict.clear()
print(my_dict)
print(diction2)
