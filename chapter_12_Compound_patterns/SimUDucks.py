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

class Goose():
    def honk(self):
        return "Honk"

class DuckAdapter(Quackable):
    def __init__(self,goose:Goose):
        self.goose=goose
    def quack(self):
        return self.goose.honk()

        
