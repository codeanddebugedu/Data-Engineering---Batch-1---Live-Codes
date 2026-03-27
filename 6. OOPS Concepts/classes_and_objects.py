class Student:
    # Constructor - Method
    def __init__(self, roll_no: int, name: str, standard: str, age: int):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.standard = standard
        self.school = "DPS"
        self.city = "Surat"

    def display(self):
        print(
            f"Roll no = {self.roll_no}, Name = {self.name}, Age = {self.age}, Standard = {self.standard}. School = {self.school}"
        )


s1 = Student(1, "Anirudh", "8th-A", 18)
s1.display()


l1 = list()
print(l1)
