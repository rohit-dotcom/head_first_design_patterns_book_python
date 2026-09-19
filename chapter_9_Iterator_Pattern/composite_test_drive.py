from composite_menu import MenuComponent,Menu,PancakeHouseMenu,MenuItem,DinerMenu,CafeMenu
from new_waiterss import Waitress

if __name__=='__main__':
    pancake_menu=PancakeHouseMenu()
    diner_menu=DinerMenu()
    cafe_menu=CafeMenu() 
    dessert_menu=Menu("Dessert Menu","Contains Desserts")
    dessert_menu.add(MenuItem('Apple Pie',"Apple Pie with flakey crust, topped with Vanilla Ice Cream",True,1.59))
    diner_menu.add(MenuItem('Pasta','Pasta with spaghetti and Marinara sause, and a slice of sour dough bread',True,3.99))
    diner_menu.add(dessert_menu)
    all_menu=Menu("All Menus","Contains All Menus")
    all_menu.add(pancake_menu)
    all_menu.add(diner_menu)
    all_menu.add(cafe_menu)
    waitress=Waitress(all_menu)

    waitress.printMenu()