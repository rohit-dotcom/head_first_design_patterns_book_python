
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
    

