from abc import ABC,abstractmethod

class Pizza(ABC):
    name:str

    dough:Dough
    sauce:Sauce
    Veggies:set()
    cheese:Cheese()
    pepperoni:Pepperoni()
    clam:Clam()

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
    def __init__(self,ingredients_factory:ingredientsFactory):
        self.ingredient_factory=self.ingredient_factory
    


    def create_ingredients(self):
        print(f"Preparing + {name}")
        dough=self.ingredient_factory.create_dough()
        sauce=self.ingredient_factory.create_sauce()
        dheese=self.ingredient_factory.create_cheese()
     
        


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

class Dough(ABC):
    pass

class Sauce(ABC):
    pass
class Cheese(ABC):
    pass
class Clam(ABC):
    pass
class Pepperoni(ABC):
    pass
class Veggies(ABC):
    pass

class Thin_Crust_Dough(Dough):
    pass
class Very_Thin_Crust_Dough(Dough):
    pass
class Thick_Crust_Dough(Dough):
    pass

class MozerellaCheese(Cheese):
    pass

class ReggianoCheese(Cheese):
    pass
class GoatCheese(Cheese):
    pass

class MarinaraSauce(Sause):
    pass
class TomatoPlumSauce(Sauce):
    pass
class BruchettaSauce(Sauce):
    pass
class FrozenClam(Clam):
    pass
class FreshClam(Clam):
    pass
class slicedPepperoni(Pepperoni):
    pass
class Garlic():
    pass
class Onion():
    pass
class Mushroom():
    pass
class RedPepper():
    pass
class BlackOlives():
    pass
class Spinach():
    pass
class EggPlant():
    pass


class ingredientsFactory(ABC):

    @abstractmethod
    def create_dough(self)->Dough:
        pass

    @abstractmethod
    def create_sauce(self)->Souce:
        pass

    @abstractmethod
    def create_cheese(self)->Cheese:
        pass
    
    @abstractmethod
    def create_veggies(self)->Veggies:
        pass

    @abstractmethod
    def create_pepproni(self)->Pepperoni:
        pass

    @abstractmethod
    def create_clam(self)->Clam:
        pass


class NY_ingredients_factory(ingredientsFactory):
    def create_dough(self):
        return Thin_Crust_Dough()

    def  create_cheese(self):
        return ReggianoCheese()

    def create_clam(self):
        return FreshClam()

    def create_pepproni(self):
        return slicedPepperoni()

    def create_sauce(self):
        return MarinaraSauce()

    def create_veggies(self):
        veggies= {Garlic(),Onion(),Mushroom()}
        return veggies  

class Chicago_ingredients_factory(ingredientsFactory):
    def create_dough(self):
        return Thick_Crust_Dough()

    def  create_cheese(self):
        return MozerellaCheese()

    def create_clam(self):
        return FrozenClam()

    def create_pepproni(self):
        return slicedPepperoni()

    def create_sauce(self):
        return TomatoPlumSauce()

    def create_veggies(self):
        veggies= {BlackOlives(),Spinach(),EggPlant()}
        return veggies  
    

