from abc import ABC,abstractmethod



class WeaponBehaviour(ABC):

    @abstractmethod
    def use_weapon(self):
        pass

class Character():
    def __init__(self,weapon_behavriour:WeaponBehaviour=None):
        if weapon_behavriour:
            self.weapon_behaviour=weapon_behavriour

    def fight(self):
        return self.weapon_behaviour.use_weapon()

    def set_weapon_behaviour(self,weapon_behaviour:WeaponBehaviour):
            self.weapon_behaviour=weapon_behaviour


class KnifeBehaviour(WeaponBehaviour):
    def use_weapon(self):
        return 'use knife'

class GunBehaviour(WeaponBehaviour):
    def use_weapon(self):
        return 'use gun'

class King(Character):

    def __init__(self,):
        self.weapon_behaviour=GunBehaviour()

class Bandit(Character):

    def __init__(self,):
        self.weapon_behaviour=KnifeBehaviour()

    
    