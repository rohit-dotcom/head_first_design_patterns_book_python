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

class PancakeHouseMenu():
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

class DinerMenu():
    def __init__(self,menuItem:List=None):
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

        

