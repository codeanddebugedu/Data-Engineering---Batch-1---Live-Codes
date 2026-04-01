# my_list = [i for i in range(1, 1000000000)]

# for num in my_list:
#     print(num)

numbers = (i for i in range(1, 1000))
print(numbers)
print(type(numbers))
print(next(numbers))

number_list = list(numbers)
print(number_list)
