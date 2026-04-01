try:
    num = int(input("Enter a number = "))
    result = 100 / num
    print(f"Result = {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please input a correct integer")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error has occurred = {e}")
    print(f"Type of error = {type(e)}")
except:
    print("Some error occurred")
