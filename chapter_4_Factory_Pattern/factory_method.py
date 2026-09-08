from abc import ABC,abstractmethod

class Pizza(ABC):
    name:str
    dough:str
    sauce:str
    cheese:str
    def __init__(self):
        self.toppings=set()

    
    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Kneading  {self.dough}')
        print(f'Adding  {self.sauce}')
        print(f'adding toppings:')
        all_toppings=''
        for topping in self.toppings:
            all_toppings+=f'    {topping}, '
        print(f'{all_toppings}')

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

class NYCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name='NY style sauce and cheese pizza'
        self.dough='Thin crust dough'
        self.sauce='Marinara Sauce'
        self.toppings.add('Grated Reggiano Cheese')

class NYPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name='NY style sauce and Pepperoni pizza'
        self.dough='Thin crust dough'
        self.sauce='Marinara Sauce'
        self.toppings.add('Grated Reggiano Cheese')


class NYveggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name='NY style sauce and Veggie pizza'
        self.dough='Thin crust dough'
        self.sauce='Marinara Sauce'
        self.toppings.add('Grated Reggiano Cheese')


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name='Chicago style sauce and cheese pizza'
        self.dough='Thick crust dough'
        self.sauce='Plum Tomato Sauce'
        self.toppings.add('Shredded Mozzarella Cheese')


    

class ChicagoPepperoniPizza(Pizza):
    pass



class ChicagoveggiePizza(Pizza):
    pass



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
