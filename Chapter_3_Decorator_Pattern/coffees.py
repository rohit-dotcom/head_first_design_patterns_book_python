from abc import ABC,abstractmethod

class Beverage(ABC):
    description:str="unknow beverage"

    def get_description(self):
        return Beverage.description


    @abstractmethod
    def cost(self,):
        pass

class CondimentDecorator(Beverage):
    beverage:Beverage
    @abstractmethod
    def get_description(self):
        pass

class Expresso(Beverage):

    def __init__(self):
        Beverage.description="Expresso"   

    def cost(self):
        return 1.99

class House_Blend(Beverage):

    def __init__(self):
        Beverage.description="House Blend"

    def cost(self):
        return 0.89

class Whip(CondimentDecorator):

    def __init__(self,beverage:Beverage):
        self.beverage=beverage

    def get_description(self):
        return self.beverage.get_description()+", whip"

    def cost(self):
        return self.beverage.cost()+0.1


class Soy(CondimentDecorator):

    def __init__(self,beverage:Beverage):
        self.beverage=beverage

    def get_description(self):
        return self.beverage.get_description()+", soy"

    def cost(self):
        return self.beverage.cost()+0.15



    