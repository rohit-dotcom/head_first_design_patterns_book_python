from menus import DinerMenu,PancakeHouseMenu,Iterator

class Waitress():
    def __init__(self, dinerMenu:DinerMenu,pancakeMenu:PancakeHouseMenu):
        self.diner_menu=dinerMenu
        self.pancakeMenu=pancakeMenu


    def printMenu(self,iterator:Iterator):
         
        while iterator.hasNext():
            item=iterator.next()
            print(item.getName())
            print(item.getDescription())
            print(item.getPrice())
            print('-'*20)

    def printAllMenu(self):
        print('Printing lunch menu items:')
        self.printMenu(self.diner_menu.createIterator())
        print('-'*50)
        print('Printing breakfast  items:')
        self.printMenu(self.pancakeMenu.createIterator())
        print('-'*50)



            
            