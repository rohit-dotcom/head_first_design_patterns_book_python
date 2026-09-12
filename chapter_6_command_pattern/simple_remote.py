from abc import ABC,abstractmethod

class commantInterface(ABC):
    @abstractmethod
    def execute():
        pass

class Light():

    def on(self,):
        return "This light is on!"

class GarageDoor():

    def open(self,):
        return "This Garage Door is opened!"

class GaragerDoorOpenCommand(commantInterface):

    def __init__(self,garageDoor:GarageDoor):
        self.garage_door=garageDoor

    def execute(self):
        return self.garage_door.open()


class LightOnCommand(commantInterface):
    def __init__(self,light:Light):
        self.light=light

    def execute(self):
        return self.light.on()


class simpleRemote():

    def __init__(self):
        self.slot=None

    def set_command(self,command:commantInterface):

        self.slot=command

    def button_pressed(self):

        return self.slot.execute()