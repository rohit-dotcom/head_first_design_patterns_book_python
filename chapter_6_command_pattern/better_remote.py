from abc import ABC,abstractmethod
import numpy as np

class Light(ABC):
    def on():
        pass
    def off():
        pass

class KitchenLight(Light):

    def on(self):
        return "This Kitchen Light is On"
    def off(self):
            return "This Kitchen Light is off"

class LivingRoomLight(Light):

    def on(self):
        return "This Living Room Light is On"
    def off(self):
            return "This Living Room Light is off"

class CellingFan():

    def high(self):
        return "This celling fan is on"

    def off(self):
        return "This celling fan is off"

class commandInterface(ABC):

    def execute(self):
        pass


class LightsOnCommand(commandInterface):

    def __init__(self,light:Light):
        self.light=light

    def execute(self):
        return self.light.on()

class LightsOFFCommand(commandInterface):

    def __init__(self,light:Light):
        self.light=light

    def execute(self):
        return self.light.off()

class CellingFanHighCommand(commandInterface):

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        return self.fan.high()

class CellingFanOffCommand(commandInterface):

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        return self.fan.off()

class RemoteControl():

    def __init__(self):
        self.onCommands=[None]*7
        self.offCommands=[None]*7


    def set_command(self,slot,offcommand:commandInterface,onCommand:commandInterface):
        self.onCommands[slot]=onCommand
        self.offCommands[slot]=offcommand

    def onButtonWasPressed(self,slot):
        return self.onCommands[slot].execute()

    def offButtonWasPressed(self,slot):
        return self.offCommands[slot].execute()

    def __repr__(self):
        remote_string='The remote has following slots and commands\n'
        for i in range(len(self.onCommands)):
            remote_string+=f'slot:{i} onCommand:{self.onCommands[i].__class__.__name__}  offCommands:{self.offCommands[i].__class__.__name__}\n'
        remote_string+='-'*50
        return remote_string




