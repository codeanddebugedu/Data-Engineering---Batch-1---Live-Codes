my_list = ["Anirudh", 54, 33.343, "Khurana", "Surat"]
# for item in my_list:
#     print(item)

my_list = iter(my_list)


while True:
    try:
        r = next(my_list, None)
        print(r)
    except StopIteration:
        break
