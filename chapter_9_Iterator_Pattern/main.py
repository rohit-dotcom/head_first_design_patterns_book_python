from waiteress import Waitress
from menus import DinerMenu,PancakeHouseMenu,CafeMenu


if __name__=="__main__":
    panckae_menu=PancakeHouseMenu()
    diner_menu=DinerMenu()
    cafe_menu=CafeMenu()

    waitress=Waitress(diner_menu,panckae_menu,cafe_menu)

    waitress.printAllMenu()