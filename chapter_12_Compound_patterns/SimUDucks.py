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
    def __init__(self,goose:Quackable):
        self.goose=goose
    def quack(self):
        return self.goose.honk()

class QuackCounter(Quackable):
    count=0
    def __init__(self,duck:Quackable):
        self.duck=duck
        

    def quack(self,):
        QuackCounter.count+=1
        return self.duck.quack()

    def getCount(self):
        return QuackCounter.count
        
