# 1 to 100 only prime numbers
def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [i for i in range(2, 101) if is_prime(i)]
print(my_list)
