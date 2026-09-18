from menus import DinerMenu,PancakeHouseMenu,Iterator,CafeMenu

class Waitress():
    def __init__(self, menuList=[]):
        self.menuList=menuList


    def printMenu(self,iterator:Iterator):
         
        while iterator.hasNext():
            item=iterator.next()
            print(item.getName())
            print(item.getDescription())
            print(item.getPrice())
            print('-'*20)

    def printAllMenu(self):
        for menu in self.menuList:
            print('-'*50)
            self.printMenu(menu.createIterator())
            print('-'*50)
       