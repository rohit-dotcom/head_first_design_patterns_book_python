
from factory_method import ChicagoPizzaStore,NYPizzaStore

if __name__=="__main__":
    ny_store=NYPizzaStore()
    ny_store.orderPizza('cheese')
    print('-'*50)
    ch_store=ChicagoPizzaStore()
    ch_store.orderPizza('cheese')