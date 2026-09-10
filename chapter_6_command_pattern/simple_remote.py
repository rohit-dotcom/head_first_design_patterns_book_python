from abc import ABC,abstractmethod

class commantInterface(ABC):
    @abstractmethod
    def execute():
        pass

class Light():

    def on(self,):
        return "This light is on!"


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