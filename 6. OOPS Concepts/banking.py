class Banking:
    def __init__(self, acc_no: int, name: str, balance: int = 0) -> None:
        self.acc_no: int = acc_no
        self.name: str = name
        self.balance: int = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        self.show_balance()

    def show_balance(self) -> None:
        print(f"Bank balance of account {self.acc_no} is Rs.{self.balance}")

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            self.show_balance()

    def transfer(self, to_account: "Banking", amount):
        to_account.balance += amount
        self.balance -= amount


acc1 = Banking(1, "Anirudh", 0)
print(type(acc1))
acc1.deposit(1000)

acc2 = Banking(2, "Vandana", 0)
acc1.transfer(acc2, 300)

acc1.show_balance()
acc2.show_balance()
