from typing import List

class MenuIsFull(Exception):
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

    def getMenuItems(self):
        return self.menuItems

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

    def getMenuItems(self):
        return self.menuItems
        

