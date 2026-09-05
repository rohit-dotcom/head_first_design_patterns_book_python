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


class ChicagoCheesePizza(Pizza):

    def bake(self):
        return "Baking cheese pizza!"

    def cut(self):
        return "Cutting in square pieces"

    def box(self):
        return "Boxing cheese pizza"
    

class ChicagoPepperoniPizza(Pizza):

    def bake(self):
        return "Baking pepperoni pizza!"

    def cut(self):
        return "Cutting in diagonal pieces"

    def box(self):
        return "Boxing pepperoni pizza"


class ChicagoveggiePizza(Pizza):

    def bake(self):
        return "Baking veggie pizza!"

    def cut(self):
        return "Cutting in triangular pieces"

    def box(self):
        return "Boxing Chichago veggie pizza"

class PizzaStore(ABC):

    
    def orderPizza(self,type)->Pizza:
        pizza:Pizza

        pizza=self.create_pizza(type)

        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self,type):
        pass

class NYPizzaStore(PizzaStore):


    def create_pizza(self,type):
        if type=="cheese":
            pizza= NYCheesePizza()
            
        if type=="pepperoni":
            pizza= NYPepperoniPizza()
                
        if type=="veggie":
            pizza=NYveggiePizza()
        return pizza

class ChicagoPizzaStore(PizzaStore):


    def create_pizza(self,type):
        if type=="cheese":
            pizza= ChicagoCheesePizza()
            
        if type=="pepperoni":
            pizza= ChicagoPepperoniPizza()
                
        if type=="veggie":
            pizza=ChicagoveggiePizza()
        return pizza
