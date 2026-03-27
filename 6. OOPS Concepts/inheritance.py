class Animal:
    def __init__(self, name: str, color: str, age: int) -> None:
        self.name = name
        self.color = color
        self.age = age

    def eat(self):
        print("I'm Eating")

    def sleep(self):
        print("I'm Sleeping")


class Sparrow(Animal):
    def __init__(
        self, name: str, color: str, age: int, city: str, state: str, eyes: int = 2
    ):
        super().__init__(name, color, age)
        self.city = city
        self.state = state
        self.eyes = eyes

    def fly(self):
        print("I'm flying")

    def display_info(self):
        print(f"Name = {self.name}, color = {self.color}, age = {self.age}")
        print(f"City = {self.city}, State = {self.state}")


s = Sparrow("Jackyyy", "Brown", 3, "Surat", "Guj")
s.display_info()
