class Count:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


count = Count(1, 4)
for num in count:
    print(num)
# while True:
#     try:
#         print(next(count))
#     except StopIteration:
#         break
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
