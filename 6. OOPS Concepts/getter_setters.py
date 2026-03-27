class Child:
    def __init__(self, address) -> None:
        self.__address = address

    # Setters
    def update_address(self, new_address):
        self.__address = new_address

    # Getters
    def get_address(self):
        return self.__address


child = Child("Surat")
child.update_address("Delhi")
print(child.get_address())
