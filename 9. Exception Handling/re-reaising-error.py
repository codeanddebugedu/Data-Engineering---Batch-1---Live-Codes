def elgible(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be neg")
        if age >= 0 and age < 18:
            raise ValueError("Not elible to vote")
    except ValueError as e:
        print("-----1-----")
        raise
    print("Done")


try:
    elgible(-100)
except ValueError as e:
    print("-----2-----")
    print(e)
except:
    print("-----3-----")
    print("Some error occurred")
