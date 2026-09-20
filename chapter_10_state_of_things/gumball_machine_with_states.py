from __future__ import annotations
from abc import ABC,abstractmethod
import random

class State(ABC):
    
    @abstractmethod
    def insertQuarter():
        pass

    @abstractmethod
    def turnCrank():
        pass

    @abstractmethod
    def ejectQuarter():
        pass

    @abstractmethod
    def dispense():
        pass


class HasQuarter(State):
    def __init__(self,gumball_machine:Gumball_Machine):
        self.gumball_machine=gumball_machine

    def insertQuarter(self):
        print('You already have inserted a quarter')

    def turnCrank(self):
        print("You will get a gumball")
        winner=random.randint(0,10)
        if winner==0 and self.gumball_machine.count>0:

            self.gumball_machine.setState(self.gumball_machine.getWinnerstate())
        else:
            self.gumball_machine.setState(self.gumball_machine.getSoldstate())

    def ejectQuarter(self):
        print("Ejecting Your quarter")
        self.gumball_machine.setState(self.gumball_machine.getNoQuarterstate())

    def dispense(self):
        print("Turn crank first")


class Sold(State):
    def __init__(self,gumball_machine:Gumball_Machine):
        self.gumball_machine=gumball_machine

    def insertQuarter(self):
        print('You already getting a gumball why you are inserting another quarter')

    def turnCrank(self):
        print("You have already turned crank")

    def ejectQuarter(self):
        print("You have already got a gumball")

    def dispense(self):
        print("Rolling out a gumball")
        self.gumball_machine.count-=1
        if self.gumball_machine.count==0:
            self.gumball_machine.setState(self.gumball_machine.getSoldOutstate())
        else:
            self.gumball_machine.setState(self.gumball_machine.getNoQuarterstate())

class NoQuarter(State):
    def __init__(self,gumball_machine:Gumball_Machine):
        self.gumball_machine=gumball_machine

    def insertQuarter(self):
        print('You have inserted quarter')
        self.gumball_machine.setState(self.gumball_machine.getHasQuarterstate())

    def turnCrank(self):
        print("Insert quarter first")

    def ejectQuarter(self):
        print("Insert quarter first")

    def dispense(self):
        print("Insert quarter first")

class SoldOut(State):
    def __init__(self,gumball_machine:Gumball_Machine):
        self.gumball_machine=gumball_machine

    def insertQuarter(self):
        print('You cant the machine is sold out')

    def turnCrank(self):
        print('You havent inserted a quarter')

    def ejectQuarter(self):
        print('You havent inserted a quarter')

    def dispense(self):
        print('You cant the machine is sold out')


class Winner(State):
    def __init__(self,gumball_machine:Gumball_Machine):
        self.gumball_machine=gumball_machine

    def insertQuarter(self):
        print('You already getting a gumball why you are inserting another quarter')

    def turnCrank(self):
        print("You have already turned crank")

    def ejectQuarter(self):
        print("You have already got a gumball")

    def dispense(self):
        print("You are a winner!!, Rolling out 2 gumballs")
        self.gumball_machine.count-=2
        if self.gumball_machine.count==0:
            self.gumball_machine.setState(self.gumball_machine.getSoldOutstate())
        else:
            self.gumball_machine.setState(self.gumball_machine.getNoQuarterstate())



class Gumball_Machine():

    def __init__(self,count):
        self.hasQuarter=HasQuarter(self)
        self.noQuarter=NoQuarter(self)
        self.sold=Sold(self)
        self.soldOut=SoldOut(self)
        self.winner=Winner(self)
        self.count=count
        self.state=self.soldOut

        if self.count>0:
            self.state=self.noQuarter

    def getSoldOutstate(self):
        return self.soldOut
    def getNoQuarterstate(self):
        return self.noQuarter
    def getHasQuarterstate(self):
        return self.hasQuarter
    def getSoldstate(self):
        return self.sold
    def getSoldOutstate(self):
        return self.soldOut
    def getWinnerstate(self):
            return self.winner

    def insertQuarter(self):
        self.state.insertQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def dispense(self):
        self.state.dispense()

    def setState(self,state:State):
        self.state=state

    def refill(self,numberOfGumballs:int):
        self.count+=numberOfGumballs
        self.setState(self.getNoQuarterstate())

    



              


