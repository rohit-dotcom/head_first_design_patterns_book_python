from abc import ABC,abstractmethod

class Pizza(ABC):

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

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

class simplePizzaFactory():
    pizza:Pizza=None

    def get_pizza(self,type):
        if type=="cheese":
            pizza= CheesePizza()
            
        if type=="pepperoni":
            pizza= PepperoniPizza()
                
        if type=="veggie":
            pizza= veggiePizza()
        return pizza

class NYCheesePizza(Pizza):

    def bake(self):
        return "Baking cheese pizza!"

    def cut(self):
        return "Cutting in square pieces"

    def box(self):
        return "Boxing cheese pizza"
    

class NYPepperoniPizza(Pizza):

    def bake(self):
        return "Baking pepperoni pizza!"

    def cut(self):
        return "Cutting in diagonal pieces"

    def box(self):
        return "Boxing pepperoni pizza"


class NYveggiePizza(Pizza):

    def bake(self):
        return "Baking veggie pizza!"

    def cut(self):
        return "Cutting in triangular pieces"

    def box(self):
        return "Boxing NYveggie pizza"



class NYPizzaFactory():
    pizza:Pizza=None

    def get_pizza(self,type):
        if type=="cheese":
            pizza= NYCheesePizza()
            
        if type=="pepperoni":
            pizza= NYPepperoniPizza()
                
        if type=="veggie":
            pizza= NYveggiePizza()
        return pizza

class PizzaStore():
    def __init__(self,factory:simplePizzaFactory):
        self.factory=factory
    
    def orderPizza(self,type)->Pizza:
        pizza:Pizza

        pizza=self.factory.get_pizza(type)

        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

