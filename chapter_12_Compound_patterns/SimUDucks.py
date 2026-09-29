from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

class Observable(ABC):
    @abstractmethod
    def add_observer():
        pass
    @abstractmethod
    def remove_observer():
        pass
    @abstractmethod
    def notifyObservers():
        pass


class Quackable(Observable):
    @abstractmethod
    def quack():
        pass

class Observer():
    def __init__(self,name:str,):
        self.name=name
   
    def update(self,observable:Observable):
        print(f"{self.name} observed a Quack ")


class QuackObservable(Observable):
    def __init__(self,duck:Quackable):
        self.observers:List[Observer]=[]
        self.duck=duck

    def add_observer(self,observer:Observer):
        self.observers.insert(-1,observer)

    def remove_observer(self,observer:Observer):
        self.observers.remove(-1,observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.duck)

class MallardDuck(Quackable):
    quack_observable:QuackObservable
    def __init__(self):
        self.quack_observable=QuackObservable(self)
        
    def quack(self):
        self.notifyObservers()
        return f"Quack"

    def add_observer(self,observer:Observer):
        self.quack_observable.add_observer(observer)
    def remove_observer(self,observer:Observer):
        self.quack_observable.remove_observer(observer)

    def notifyObservers(self):
        self.quack_observable.notifyObservers()

class RubberDuck(QuackObservable):
    def __init__(self):
        self.quack_observable=QuackObservable(self)
            
    def quack(self):
        self.notifyObservers()
        return f"Squeak"

    def add_observer(self,observer:Observer):
            self.quack_observable.add_observer(observer)
    def remove_observer(self,observer:Observer):
        self.quack_observable.remove_observer(observer)

    def notifyObservers(self):
        self.quack_observable.notifyObservers()
class DuckWistle(QuackObservable):
    def __init__(self):
        self.quack_observable=QuackObservable(self)
                
    def quack(self):
        self.notifyObservers()
        return f"Kwaq"

    def add_observer(self,observer:Observer):
        self.quack_observable.add_observer(observer)
    def remove_observer(self,observer:Observer):
        self.quack_observable.remove_observer(observer)

    def notifyObservers(self):
        self.quack_observable.notifyObservers()

class Goose():    
    def honk(self):
        return "Honk"

class DuckAdapter(QuackObservable):
    def __init__(self,goose:Quackable):
        self.goose=goose
        self.quack_observable=QuackObservable(self)
                
    def quack(self):
        self.notifyObservers()
        return self.goose.honk()

    def add_observer(self,observer:Observer):
        self.quack_observable.add_observer(observer)
    def remove_observer(self,observer:Observer):
        self.quack_observable.remove_observer(observer)
 
    def notifyObservers(self):
        self.quack_observable.notifyObservers()

class QuackCounter(QuackObservable):
    count=0
    def __init__(self,duck:Quackable):
        self.duck=duck
        self.quack_observable=QuackObservable(self)
        

    def quack(self,):
        self.quack_observable.notifyObservers()
        QuackCounter.count+=1
        return self.duck.quack()
    def add_observer(self,observer:Observer):
        self.quack_observable.add_observer(observer)
    def remove_observer(self,observer:Observer):
        self.quack_observable.remove_observer(observer)
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


            

