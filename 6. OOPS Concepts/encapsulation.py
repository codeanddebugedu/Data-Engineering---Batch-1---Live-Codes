# Data Hiding, Public, Protected and Private (Access modifiers)


class Father:
    def __init__(self, father_name: str, balance: int) -> None:
        self.father_name = father_name
        self._balance = balance

    def __withdraw_balance(self, amount: int):
        if amount > self._balance:
            print("Not enough balance")
        else:
            self._balance -= amount
            print(f"Withdraw Rs.{amount}, Remaining balance = Rs.{self._balance}")

    def deposit(self, amount: int):
        self._balance += amount
        print(f"Deposit Rs.{amount}, Remaining balance = Rs.{self._balance}")

    def display_father_balance(self):
        print(f"Remaining balance = Rs.{self._balance}")


class Child(Father):
    def __init__(self, father_name: str, balance: int, child_name: str) -> None:
        super().__init__(father_name, balance)
        self.child_name = child_name

    def transfer_to_father(self, amount: int):
        self._balance += amount


child = Child("Sanjay", 1000, "Anirudh")
child.transfer_to_father(1000)
child.display_father_balance()
# print(child.__balance)
# child.__balance = 10000
# print(child.__balance)
