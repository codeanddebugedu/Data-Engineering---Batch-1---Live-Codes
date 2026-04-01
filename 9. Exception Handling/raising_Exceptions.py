def elgible(age):
    if age < 0:
        raise ValueError("Age cannot be neg")
    if age >= 0 and age < 18:
        raise ValueError("Not elible to vote")


try:
    elgible(-100)
except ValueError as e:
    print(e)
except:
    print("Some error occurred")
else:
    print("You can vote")
finally:
    print("Age Checking done")
