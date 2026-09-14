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
        if self.customerWantsCondiments():
            self.add_condiments()

    def customerWantsCondiments(self):
        return False

class Coffee(CafinatedBeverage):
    def brew(self):
        print("Letting Coffee grinds brew in hot water")

    def add_condiments(self):
        print("Adding milk and sugar")

    def customerWantsCondiments(self):
        user_input=self.getUserInput()
        if str.lower(user_input)=='y':
            return True
        else:
            return False
    def getUserInput(self):
        userInput=input("Do you wand to add milk and sugar?(y/n)")
        return userInput
    

class Tea(CafinatedBeverage):
    def brew(self):
        print("Letting tea leaves steep in boiling with water")

    def add_condiments(self):
        print("Adding lemon")
