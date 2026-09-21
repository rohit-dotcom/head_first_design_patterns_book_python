from abc import ABC,abstractmethod

class Quackable(ABC):
    @abstractmethod
    def quack():
        pass

class MallardDuck(Quackable):
    def quack(self):
        return "Quack"

class RubberDuck(Quackable):
    def quack(self):
        return "Squeak"

class DuckWistle(Quackable):
    def quack(self):
        return "Kwaq"


