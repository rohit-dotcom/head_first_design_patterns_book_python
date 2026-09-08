from abc import ABC,abstractmethod

from abstract_factory import ingredientsFactory

class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

    def getName(self):
        return name

    def setName(self,name:str):
        self.name=name

class CheesePizza(Pizza):

     
    def bake(self):
        return "Baking cheese pizza!"

    def cut(self):
        return "Cutting in square pieces"

    def box(self):
        return "Boxing cheese pizza"
    

class PepperoniPizza(Pizza):
    
        

    def bake(self):
        return "Baking pepperoni pizza!"

    def cut(self):
        return "Cutting in diagonal pieces"

    def box(self):
        return "Boxing pepperoni pizza"


class veggiePizza(Pizza):

    def bake(self):
        return "Baking veggie pizza!"

    def cut(self):
        return "Cutting in triangular pieces"

    def box(self):
        return "Boxing veggie pizza"

