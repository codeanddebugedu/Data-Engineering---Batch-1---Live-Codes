def count(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for num in count(1, 5):
    print(num)
