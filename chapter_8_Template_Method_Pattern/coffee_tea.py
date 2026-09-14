from abc import ABC,abstractmethod

class CafinatedBeverage(ABC):

    def boil_hot_water(self):
        print('Hot water is boiling')

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print('Pouring in cup')

    @abstractmethod
    def add_condiments(self):
        pass

    def prepareBeverage(self):
        self.boil_hot_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

class Coffee(CafinatedBeverage):
    def brew(self):
        print("Letting Coffee grinds brew in hot water")

    def add_condiments(self):
        print("Adding milk and sugar")


class Tea(CafinatedBeverage):
    def brew(self):
        print("Letting tea leaves steep in boiling with water")

    def add_condiments(self):
        print("Adding lemon")
