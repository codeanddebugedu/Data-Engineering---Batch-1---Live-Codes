class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectange(Shape):
    def __init__(self, l, b) -> None:
        self.l = l
        self.b = b

    def area(self):
        print(f"Rectangle area = {self.l * self.b}")

    def perimeter(self):
        print(f"Rectangle perimeter = {2* (self.l +self.b)}")


class Circle(Shape):
    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        print(f"Rectangle area = {3.14*self.r*self.r}")

    def perimeter(self):
        print(f"Rectangle perimeter = {2*3.14*self.r}")
