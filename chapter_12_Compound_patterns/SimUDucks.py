from abc import ABC,abstractmethod
from typing import List

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
    @classmethod
    def getCount(self):
        return QuackCounter.count

class DuckFactory(ABC):
    @abstractmethod
    def createMallardDuck():
        pass
    @abstractmethod
    def createRubberDuck():
        pass
    @abstractmethod
    def createdDuckWistle():
        pass
    @abstractmethod
    def createDuckAdapter():
        pass

class CounterDuckFactory(DuckFactory):

    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())

    def createdDuckWistle(self):
        return QuackCounter(DuckWistle())

    def createDuckAdapter(self):
        return QuackCounter(DuckAdapter(Goose()))
    
class NormalDuckFactory(DuckFactory):

    def createMallardDuck(self):
        return MallardDuck()

    def createRubberDuck(self):
        return RubberDuck()

    def createdDuckWistle(self):
        return DuckWistle()

    def createDuckAdapter(self):
        return DuckAdapter(Goose())

class Flock(Quackable):
    def __init__(self,ducks:List[Quackable]=[]):
        self.ducks=ducks

    def add(self,duck):
        self.ducks.insert(-1,duck)

    def remove(self,duck):
        self.ducks.remove(duck)

    def quack(self):
        for duck in self.ducks:
            duck.quack()

    