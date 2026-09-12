from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack():
        pass

    @abstractmethod
    def fly():
        pass

class MallardDuck(Duck):
    def __init__(self,name:str):
        self.name=name

    def quack(self):
        return "This Mallard Duck Quacks"

    def fly(self):
        return "This Mallard Duck Flys"


class Turkey():
    def __init__(self,name:str):
        self.name=name

    def gobble(self):
        return "this turkey gobbles"

    def fly_short_distance(self):
        return "this turkey flies short distance"

class turkeyAdapter(Duck):
    def __init__(self,turkey:Turkey):
        self.turkey=turkey

    def quack(self):
        return self.turkey.gobble()

    def fly(self):
        fly_string=''
        for i in range(5):
            fly_string+=self.turkey.fly_short_distance()+'\n'
        return fly_string
