from abc import ABC,abstractmethod
from typing import List


class commandInterface(ABC):

    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class Light(ABC):
    def on():
        pass
    def off():
        pass
    def dim(self):
        return "this light is dim"

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

    HIGH=3
    MEDIUM=2
    LOW=1
    OFF=0
    speed=None

    def __init__(self,location:str):
        self.location=location
        CellingFan.speed=CellingFan.OFF
        
    def high(self):
        CellingFan.speed=CellingFan.HIGH
        return "This celling fan is high"
    def medium(self):
        CellingFan.speed=CellingFan.MEDIUM
        return "This celling fan is medium"
    def low(self):
        CellingFan.speed=CellingFan.LOW
        return "This celling fan is low"
    def off(self):
        CellingFan.speed=CellingFan.OFF
        return "This celling fan is off"
    def get_speed(self)->int:
        return CellingFan.speed

class Stereo():
    def __init__(self,name:str):
        self.name=name

    def on(self):
        return "This Stereo is on"

    def off(self):
        return "This stereo is off"

    def setCD(self):
        return "This stereo is set to cd"

    def setRadio(self):
        return "This stereo is set to Radio"

    def setDVD(self):
        return "This stereo is set to DVD"
    def setVolumn(self):
        return "this is set Volumne for stereo"

class Hottub():
    def __init__(self,name:str):
        self.name=name

    def on(self):
        return "this hottub is on"

    def off(self):
        return "this hottub is off"

class  TV():
    def __init__(self,name:str):
        self.name=name

    def on(self):
        return "This TV is ON"

    def off(self):
        return "This tv is off"


class LightsOnCommand(commandInterface):

    def __init__(self,light:Light):
        self.light=light

    def execute(self):
        return self.light.on()

    def undo(self):
        return self.light.off()

class LightsOFFCommand(commandInterface):

    def __init__(self,light:Light):
        self.light=light

    def execute(self):
        return self.light.off()
    
    def undo(self):
        return self.light.on()
    

class CellingFanHighCommand(commandInterface):
    prev_speed=None

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        CellingFanHighCommand.prev_speed=self.fan.get_speed()    
        return self.fan.high()
    def undo(self):
        if CellingFanHighCommand.prev_speed==CellingFan.HIGH:
            return self.fan.high()
        if CellingFanHighCommand.prev_speed==CellingFan.MEDIUM:
            return self.fan.medium()
        if CellingFanHighCommand.prev_speed==CellingFan.LOW:
            return self.fan.low()
        if CellingFanHighCommand.prev_speed==CellingFan.OFF:
            return self.fan.off()

class CellingFanMediumCommand(commandInterface):
    prev_speed=None

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        CellingFanHighCommand.prev_speed=self.fan.get_speed()    
        return self.fan.medium()
    def undo(self):
        if CellingFanHighCommand.prev_speed==CellingFan.HIGH:
            return self.fan.high()
        if CellingFanHighCommand.prev_speed==CellingFan.MEDIUM:
            return self.fan.medium()
        if CellingFanHighCommand.prev_speed==CellingFan.LOW:
            return self.fan.low()
        if CellingFanHighCommand.prev_speed==CellingFan.OFF:
            return self.fan.off()

class CellingFanLowCommand(commandInterface):
    prev_speed=None

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        CellingFanHighCommand.prev_speed=self.fan.get_speed()    
        return self.fan.low()
    def undo(self):
        if CellingFanHighCommand.prev_speed==CellingFan.HIGH:
            return self.fan.high()
        if CellingFanHighCommand.prev_speed==CellingFan.MEDIUM:
            return self.fan.medium()
        if CellingFanHighCommand.prev_speed==CellingFan.LOW:
            return self.fan.low()
        if CellingFanHighCommand.prev_speed==CellingFan.OFF:
            return self.fan.off()
   

class CellingFanOffCommand(commandInterface):
    prev_speed=None

    def __init__(self,fan:CellingFan):
        self.fan=fan

    def execute(self):
        CellingFanHighCommand.prev_speed=self.fan.get_speed()    
        return self.fan.off()
    def undo(self):
        if CellingFanHighCommand.prev_speed==CellingFan.HIGH:
            return self.fan.high()
        if CellingFanHighCommand.prev_speed==CellingFan.MEDIUM:
            return self.fan.medium()
        if CellingFanHighCommand.prev_speed==CellingFan.LOW:
            return self.fan.low()
        if CellingFanHighCommand.prev_speed==CellingFan.OFF:
            return self.fan.off()

class tvOnCommand(commandInterface):
    def __init__(self,tv:TV):
        self.tv=tv

    def execute(self):
        return self.tv.on()
    def undo(self):
        return self.tv.off()
class tvOffCommand(commandInterface):
    def __init__(self,tv:TV):
        self.tv=tv

    def execute(self):
        return self.tv.off()
    def undo(self):
        return self.tv.on()

class hottubOnCommand(commandInterface):
    def __init__(self,hottub:Hottub):
        self.hottub=hottub

    def execute(self):
        return self.hottub.on()
    def undo(self):
        return self.hottub.off()
class hottubOffCommand(commandInterface):
    def __init__(self,hottub:Hottub):
        self.hottub=hottub

    def execute(self):
        return self.hottub.off()
    def undo(self):
        return self.hottub.on()


class stereoOnCommand(commandInterface):
    def __init__(self,stereo:Stereo):
        self.stereo=stereo

    def execute(self):
        return self.stereo.on()
    def undo(self):
        return self.stereo.off()
class stereoOffCommand(commandInterface):
    def __init__(self,stereo:Stereo):
        self.stereo=stereo

    def execute(self):
        return self.stereo.off()
    def undo(self):
        return self.stereo.on()

class Macros(commandInterface):

    def __init__(self,commands:List[commandInterface]):
         self.commands=commands

    def execute(self):
        output_str=''
        for command in self.commands:
            output_str+=f'{command.execute()}\n'
        return output_str

    def undo(self):
        output_str=''
        for command in self.commands:
            output_str+=f'{command.undo()}\n'
        return output_str
    

    
   
class RemoteControl():

    def __init__(self):
        self.onCommands=[None]*7
        self.offCommands=[None]*7
        self.undoCommand=None


    def set_command(self,slot,offcommand:commandInterface,onCommand:commandInterface):
        self.onCommands[slot]=onCommand
        self.offCommands[slot]=offcommand


    def onButtonWasPressed(self,slot):
        self.undoCommand=self.onCommands[slot]
        return self.onCommands[slot].execute()

    def offButtonWasPressed(self,slot):
        self.undoCommand=self.offCommands[slot]
        return self.offCommands[slot].execute()

    def undoButtonWasPressed(self):
        return self.undoCommand.undo()

    def __repr__(self):
        remote_string='The remote has following slots and commands\n'
        for i in range(len(self.onCommands)):
            remote_string+=f'slot:{i} onCommand:{self.onCommands[i].__class__.__name__}  offCommands:{self.offCommands[i].__class__.__name__}\n'
        remote_string+=f'undo: UndoCommand\n'
        remote_string+='-'*50
        return remote_string




