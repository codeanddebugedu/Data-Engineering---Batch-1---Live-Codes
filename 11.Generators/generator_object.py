def greet():
    yield "Hello"
    yield "Good"
    yield "Bye"


result = greet()
print(type(result))

print(next(result))
print(next(result))
print(next(result))
