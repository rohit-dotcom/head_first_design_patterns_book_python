from abc import ABC,abstractmethod

class Dough(ABC):
    name:str

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
    name:str='Thin crust dough'
class Very_Thin_Crust_Dough(Dough):
    name:str='Very thin crust dough'
class Thick_Crust_Dough(Dough):
    name:str='Thick crust dough'

class MozerellaCheese(Cheese):
    pass

class ReggianoCheese(Cheese):
    pass
class GoatCheese(Cheese):
    pass

class MarinaraSauce(Sauce):
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
    def create_sauce(self)->Sauce:
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
    

class Pizza(ABC):
    name:str
    dough:str
    sauce:str
    cheese:str
    def __init__(self):
        self.toppings=set()

    @abstractmethod
    def prepare(self):
       pass

    def bake(self):
        print( "Baking for 25 minutes at 350 degrees")

    def cut(self):
        print("Cutting diagonal pieces")

    
    def box(self):
        print("Boxing in the official pizzastore box")

    def getName(self):
        return self.name

    def setName(self,name:str):
        self.name=name

class CheesePizza(Pizza):
    def __init__(self,ingredient_factory:ingredientsFactory):
        self.ingredient_factory=ingredient_factory

    def prepare(self):
        self.dough=self.ingredient_factory.create_dough()
        self.sauce=self.ingredient_factory.create_dough()
        self.cheese=self.ingredient_factory.create_cheese()

class PepperoniPizza(Pizza):
    def __init__(self,ingredient_factory:ingredientsFactory):
        self.ingredient_factory=ingredient_factory

    def prepare(self):
        self.dough=self.ingredient_factory.create_dough()
        self.sauce=self.ingredient_factory.create_dough()
        self.cheese=self.ingredient_factory.create_cheese()

class VeggiePizza(Pizza):
    def __init__(self,ingredient_factory:ingredientsFactory):
        self.ingredient_factory=ingredient_factory

    def prepare(self):
        self.dough=self.ingredient_factory.create_dough()
        self.sauce=self.ingredient_factory.create_dough()
        self.cheese=self.ingredient_factory.create_cheese()



class PizzaStore(ABC):


    def orderPizza(self,type)->Pizza:
        pizza:Pizza

        pizza=self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self,type):
        pass

class NYPizzaStore(PizzaStore):


    def create_pizza(self,type):
        pizza:Pizza=None
        ingredient_factory=NY_ingredients_factory()
        if type=="cheese":
            pizza= CheesePizza(ingredient_factory)
            
        if type=="pepperoni":
            pizza= PepperoniPizza(ingredient_factory)
                
        if type=="veggie":
            pizza=VeggiePizza(ingredient_factory)
        return pizza

class ChicagoPizzaStore(PizzaStore):


    def create_pizza(self,type):
        pizza:Pizza=None
        ingredient_factory=Chicago_ingredients_factory()
        if type=="cheese":
            pizza= CheesePizza(ingredient_factory)
            
        if type=="pepperoni":
            pizza= PepperoniPizza(ingredient_factory)
                
        if type=="veggie":
            pizza=VeggiePizza(ingredient_factory)
        return pizza
