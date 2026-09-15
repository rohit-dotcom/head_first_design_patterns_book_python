from menus import DinerMenu,PancakeHouseMenu

class Waitress():
    def __init__(self, dinerMenu:DinerMenu,pancakeMenu:PancakeHouseMenu):
        self.diner_menu=dinerMenu
        self.pancakeMenu=pancakeMenu

    def printMenu(self):
        dinermenu_items=self.diner_menu.getMenuItems()
        pancakemenu_items=self.pancakeMenu.getMenuItems()
        print('Printing diner menu items:')
        for item in dinermenu_items:
            if item:
                print(item.getName())
                print(item.getDescription())
                print(item.getPrice())

        print('-'*50)
        print('Printing PancakeHouse menu items:')
        for item in pancakemenu_items:
            if item:
                print(item.getName())
                print(item.getDescription())
                print(item.getPrice())

        print('-'*50)



            
            