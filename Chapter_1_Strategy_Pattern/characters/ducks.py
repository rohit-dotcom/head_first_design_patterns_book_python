from abc import ABC,abstractmethod


class FlyBehaviour(ABC):

    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehaviour):

    def fly(self):
        return 'this duck flies with wings'

class FlyNoWay(FlyBehaviour):

    def fly(self):
        return 'this duck does not fly'

class QuackBehaviour(ABC):

    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehaviour):

    def quack(self):
        return 'this duck quacks'

class Squeal(QuackBehaviour):

    def quack(self):
        return 'this duck squeals'

class NoQuack(QuackBehaviour):

    def quack(self):
        return 'this duck does not quack'

class Duck():

    def __init__(self,fly_behaviour:FlyBehaviour=None,quack_behaviour:QuackBehaviour=None):
        if fly_behaviour is not None:
            self.fly_behaviour=fly_behaviour
        if quack_behaviour is not None:
            self.quack_behavriour=quack_behaviour

    def set_fly_behaviour(self,fly_behaviour:FlyBehaviour):
        self.fly_behaviour=fly_behaviour

    def set_quack_behaviour(self,quack_behaviour:QuackBehaviour):
        self.quack_behavriour=quack_behaviour
        

    def fly(self):
        return self.fly_behaviour.fly()

    def quack(self):
        return self.quack_behavriour.quack()

    def swim(self):
        return f'this duck can swim'


