from composite_menu import MenuComponent
class Waitress():
    def __init__(self,allMenu:MenuComponent):
        self.all_menu=allMenu

    def printMenu(self):
        self.all_menu.printIt()

