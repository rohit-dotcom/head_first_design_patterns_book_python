from better_remote import RemoteControl,LivingRoomLight,KitchenLight,LightsOnCommand,LightsOFFCommand,CellingFanHighCommand,CellingFanOffCommand,CellingFan

if __name__=="__main__":
    light=LivingRoomLight()
    LivingRoomonCommand=LightsOnCommand(light)
    LivingRoomOffcommand=LightsOFFCommand(light)
    celling_fan=CellingFan()
    celling_fan_high_command=CellingFanHighCommand(celling_fan)
    celling_fan_off_command=CellingFanOffCommand(celling_fan)
    remote=RemoteControl()
    remote.set_command(0,LivingRoomOffcommand,LivingRoomonCommand)
    remote.set_command(1,celling_fan_off_command,celling_fan_high_command)
    print(remote.onButtonWasPressed(0))
    print(remote.offButtonWasPressed(0))
    print('_'*5+'trying undo command'+'_'*5)
    print(remote.undoButtonWasPressed())
    print(remote.onButtonWasPressed(1))
    print(remote.offButtonWasPressed(1))
    

    print(remote)