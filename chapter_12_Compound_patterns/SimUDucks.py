from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

class Quackable(ABC):
    @abstractmethod
    def quack():
        pass

class Observable(ABC):
    @abstractmethod
    def add_observer():
        pass
    @abstractmethod
    def remove_observer():
        pass
    @abstractmethod
    def notify():
        pass

class Observer():
    def __init__(self,name:str,):
        self.name=name
   
    def update(self,observable:Observable):
        print(f"{self.name} observed a Quack ")

class QuackObservable(Quackable,Observable):
    def __init__(self,observers:List[Observer]=[]):
        self.observers=observers

    def add_observer(self,observer:Observer):
        self.observers.insert(-1,observer)

    def remove_observer(self,observer:Observer):
          self.observers.remove(-1,observer)

    def notify(self):
        for observer in self.observers:
            observer.update(observer)

class MallardDuck(QuackObservable):
    def __init__(self):
            super().__init__()

    def quack(self):
        self.notify()
        return f"Quack"

class RubberDuck(QuackObservable):
    def __init__(self):
        super().__init__()
    
    def quack(self):
        self.notify()
        return "Squeak"

class DuckWistle(QuackObservable):
    def quack(self):
        return "Kwaq"

class Goose():
    def honk(self):
        return "Honk"

class DuckAdapter(QuackObservable):
    def __init__(self,goose:Quackable):
        self.goose=goose
    def quack(self):
        return self.goose.honk()

class QuackCounter(QuackObservable):
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

class Flock(QuackObservable):
    def __init__(self,ducks:List[QuackObservable]=[]):
        self.ducks=ducks

    def add(self,duck):
        self.ducks.insert(-1,duck)

    def remove(self,duck):
        self.ducks.remove(duck)

    def quack(self):
        for duck in self.ducks:
            duck.quack()


            

