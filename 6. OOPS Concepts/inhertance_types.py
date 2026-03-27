# # Multi Level
# class A:
#     def abc(self):
#         print("This is abc of class A")


# class B(A):
#     def xyz(self):
#         print("This is xyz of class B")


# class C(B):
#     def pqr(self):
#         print("This is pqr of class C")


class A:
    def abc(self):
        print("This is abc of class A")


class B:
    def xyz(self):
        print("This is xyz of class B")


class C(A, B):
    def pqr(self):
        print("This is pqr of class C")
