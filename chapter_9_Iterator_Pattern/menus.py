from __future__ import annotations
from typing import List
from abc import ABC,abstractmethod


class MenuIsFull(Exception):
    pass

class EndOfIteration(Exception):
    pass

class Iterator(ABC):
    def hasNext()->bool:
        pass
    def next()->bool:
        pass

class Menu(ABC):
    @abstractmethod
    def createIterator(self):
        pass
    
class menuItem():
    def __init__(self,name:str,description:str,isVeg:bool,price:float):
        self.name=name
        self.description=description
        self.isVeg=isVeg
        self.price=price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getIsVeg(self):
        return self.isVeg

    def getPrice(self):
        return self.price

class PancakeHouseMenu(Menu):
    def __init__(self,menuItems:set=set()):
        self.menuItems=menuItems
        self.addItem('K&B Pancake Breakfast','Pancakes with scrambled Eggs and toast',
                           False,2.99)
        self.addItem('Regular Pancake Breakfast','Pancakes with fried Eggs and sausage',
                                   False,2.99)
        self.addItem('Blueberry Pancakes','Pancakes with freshly made blueberries',
                                   True,3.49)
        self.addItem('Waffles','Waffles with your choice of blueberries or strawberries',
                                   True,3.59)

    def addItem(self,name:str,description:str,isVeg:bool,price:float):
        menu_item=menuItem(name,description,isVeg,price)
        self.menuItems.add(menu_item)

    def createIterator(self):
        return PancakeHouseIterator(self.menuItems)

class PancakeHouseIterator(Iterator):
    def __init__(self,pancake_menu_items):
        self.position=0
        self.menu_items=[i for i in pancake_menu_items]

    def hasNext(self):
        if self.position<len(self.menu_items) and self.menu_items[self.position] :
            return True
        else:
            return False
    def next(self):
        if self.hasNext():
            item=self.menu_items[self.position]
            self.position+=1
            return item
        else:
            raise EndOfIteration("Reach End of Iterations")

class DinerMenu(Menu):
    def __init__(self,):
        self.max_items=6
        self.menuItems=[None]*self.max_items
        self.numberOfItems=0

        self.addItem('Vegetrain BLT','Fake Bacon with lettuce and tomato on whole wheat',
                     True,2.99)
        self.addItem('BLT','Bacon with lettuce and tomato in whole wheat',
                             False,2.99)
        self.addItem('Soup of the day','Soup of the day with a side of potato salad',
                             False,3.29)
        self.addItem('Hotdog','Hotdog with sauerkraut, relish, onions,topped with cheese',
                             False,3.05)

    def addItem(self,name:str,description:str,isVeg:bool,price:float):
        menu_item=menuItem(name,description,isVeg,price)
        if self.numberOfItems>=self.max_items:
            raise MenuIsFull("Sorry Menu Is Full , Cant add any more items")
        else:
            self.menuItems[self.numberOfItems]=menu_item
            self.numberOfItems+=1

    def createIterator(self):
        return DinerIterator(self.menuItems)

class DinerIterator(Iterator):
    def __init__(self,diner_menu_items):
        self.position=0
        self.menu_items=diner_menu_items

    def hasNext(self):
        if self.menu_items[self.position]:
            
            return True
        else:
            return False
    def next(self):
        if (self.hasNext()) and (self.menu_items[self.position] is not None):
            item=self.menu_items[self.position]
            print(f'next Item is {item.getName()}')
            self.position+=1
            return item
        
        else:
            raise EndOfIteration("Reached End of Iterations")

class CafeMenu(Menu):
    def __init__(self,):
        self.menuItems={}

        self.addItems( "Veggie Burger and Air Fries",
                      "Veggie Burger on a Whole Wheat Bun,lettuce , tomato and fries",
                      True,3.99)
        self.addItems("Soup of the day","A cup of soup of the day, with a side salad",
                      False,3.69)
        self.addItems("Burrito","A large burrito, with whole pinto beans, salsa,guacamole",
                      True,4.29)

    def addItems(self,name:str,description:str,isVeg:bool,price:float):
        self.menuItems[name]=menuItem(name,description,isVeg,price)
    

    def createIterator(self):
        return CafeMenuIterator(self.menuItems)

class CafeMenuIterator(Iterator):
    def __init__(self,cafe_menu_items:dict):
        self.menu_items=cafe_menu_items
        self.all_keys=(i for i in cafe_menu_items.keys())
        self.next_key=next(self.all_keys)

    def hasNext(self):
        if self.next_key:
            return True
        else:
            return False

    def next(self):
        if self.hasNext():
            item=self.menu_items[self.next_key]
            try:
                self.next_key=next(self.all_keys)
                return item
            except StopIteration:
                self.next_key=None
                return item
        else:
            raise EndOfIteration("Reached End of Iterations")
        

        
        

