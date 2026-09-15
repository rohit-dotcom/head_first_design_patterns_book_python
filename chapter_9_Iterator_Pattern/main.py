from waiteress import Waitress
from menus import DinerMenu,PancakeHouseMenu


if __name__=="__main__":
    panckae_menu=PancakeHouseMenu()
    diner_menu=DinerMenu()

    waitress=Waitress(diner_menu,panckae_menu)

    waitress.printMenu()