from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def speak(self):
        pass

    def whoami(self):
        print("I am a animal")


# Concrete class
class Sparrow(Animal):
    def fly(self):
        print("Sparrow is flying")

    def eat(self):
        print("Sparrow is eating")

    def speak(self):
        print("Sparrow is speaking")


s = Sparrow()
s.eat()
s.speak()
s.whoami()
