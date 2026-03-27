from random import randint


def random_number():
    return randint(1, 100)


def random_character():
    return "hajkdhwajkdwa"[randint(1, 10)]


def random_password():
    return random_character() + str(random_number())


if __name__ == "__main__":
    print("Testing this module")
    print(f"Generating random number = {random_number()}")
    print("Finished testing this module")
