from __future__ import annotations
from abc import ABC,abstractmethod

class UnsupportedOperationError(Exception):
    pass

class MenuComponent(ABC):

    def getName():
        raise UnsupportedOperationError()

    def getDescription():
        raise UnsupportedOperationError()

    def getPrice():
        raise UnsupportedOperationError()

    def isVegetarian()->bool:
        raise UnsupportedOperationError()

    def add(component:MenuComponent):
        raise UnsupportedOperationError()

    def remove(component:MenuComponent):
        raise UnsupportedOperationError()

    def getChild(i: int):
        raise UnsupportedOperationError()

    def printIt():
        raise UnsupportedOperationError()

class MenuItem(MenuComponent):

    def __init__(self,name:str,description:str,isVeg:bool,price:float):
        self.name=name
        self.description=description
        self.isVeg=isVeg
        self.price=price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def isVegetarian(self):
        return self.isVeg

    def printIt(self):
        print(f'{self.name}', end="")
        if self.isVeg:
            print(' (V)', end="")
        print(f', {self.description}')
        print(f'---- {self.price}')

class Menu(MenuComponent):
    def __init__(self,name:str,desc:str):
        self.menu_components=[]
        self.name=name
        self.description=desc

    def add(self,component:MenuComponent):
        self.menu_components.insert(-1,component)

    def remove(self,component:MenuComponent):
        self.menu_components.remove(component)

    def getChild(self,i):
        return self.menu_components[i]

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def printIt(self):
        print('-'*50)
        print(f'{self.name}',end=', ')
        print(f'{self.description}')
        print('-'*50)
        for item  in self.menu_components:
            item.printIt()


class PancakeHouseMenu(Menu):
    def __init__(self,):
        super().__init__('Pancake house Menu', 'Breakfast')

        self.add(MenuItem('K&B Pancake Breakfast','Pancakes with scrambled Eggs and toast',
                           False,2.99))
        self.add(MenuItem('Regular Pancake Breakfast','Pancakes with fried Eggs and sausage',
                                   False,2.99))
        self.add(MenuItem('Blueberry Pancakes','Pancakes with freshly made blueberries',
                                   True,3.49))
        self.add(MenuItem('Waffles','Waffles with your choice of blueberries or strawberries',
                                   True,3.59))



class DinerMenu(Menu):
    def __init__(self,):
        super().__init__('Diner Menu', 'Lunch')

        self.add(MenuItem('Vegetrain BLT','Fake Bacon with lettuce and tomato on whole wheat',
                     True,2.99))
        self.add(MenuItem('BLT','Bacon with lettuce and tomato in whole wheat',
                             False,2.99))
        self.add(MenuItem('Soup of the day','Soup of the day with a side of potato salad',
                             False,3.29))
        self.add(MenuItem('Hotdog','Hotdog with sauerkraut, relish, onions,topped with cheese',
                             False,3.05))


class CafeMenu(Menu):
    def __init__(self,):
        super().__init__('Cafe Menu', 'Dinner')

        self.add(MenuItem( "Veggie Burger and Air Fries",
                      "Veggie Burger on a Whole Wheat Bun,lettuce , tomato and fries",
                      True,3.99))
        self.add(MenuItem("Soup of the day","A cup of soup of the day, with a side salad",
                      False,3.69))
        self.add(MenuItem("Burrito","A large burrito, with whole pinto beans, salsa,guacamole",
                      True,4.29))
