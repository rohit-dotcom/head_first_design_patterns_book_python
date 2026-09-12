from better_remote import (RemoteControl,LivingRoomLight,
                            KitchenLight,LightsOnCommand,LightsOFFCommand,
                            CellingFanHighCommand,CellingFanOffCommand,
                            CellingFan,CellingFanMediumCommand,
                            Macros,TV,tvOnCommand,tvOffCommand,
                            Hottub,hottubOffCommand,hottubOnCommand,
                            Stereo,stereoOffCommand,stereoOnCommand)

if __name__=="__main__":
    light=LivingRoomLight()
    LivingRoomonCommand=LightsOnCommand(light)
    LivingRoomOffcommand=LightsOFFCommand(light)
    celling_fan=CellingFan('LivingRoom')
    celling_fan_high_command=CellingFanHighCommand(celling_fan)
    celling_fan_medium_command=CellingFanMediumCommand(celling_fan)
    celling_fan_off_command=CellingFanOffCommand(celling_fan)
    tv=TV('LivingRoom')
    tv_on_command=tvOnCommand(tv)
    tv_off_command=tvOffCommand(tv)
    stereo=Stereo("Living Room")
    stereo_on_command=stereoOnCommand(stereo)
    stereo_off_command=stereoOffCommand(stereo)
    hottub=Hottub('Garden')
    hottub_on_command=hottubOnCommand(hottub)
    hottub_off_command=hottubOffCommand(hottub)
    remote=RemoteControl()
    remote.set_command(0,celling_fan_off_command,celling_fan_medium_command)
    remote.set_command(1,celling_fan_off_command,celling_fan_high_command)
    print(remote)
    print(remote.onButtonWasPressed(0))
    print(remote.offButtonWasPressed(0))
    print('_'*5+'trying undo command'+'_'*5)
    print(remote.undoButtonWasPressed())
    print(remote.onButtonWasPressed(1))

    macro_on_command_list=[celling_fan_medium_command,tv_on_command,stereo_on_command,hottub_on_command]
    macro_off_command_list=[celling_fan_off_command,tv_off_command,stereo_off_command,hottub_off_command]
    macro_on_command=Macros(macro_on_command_list)
    macro_off_command=Macros(macro_off_command_list)
    remote.set_command(2,macro_off_command,macro_on_command,)
    print(remote)

    print('-'*5+'trying out macro on command'+'-'*50)
    print(remote.onButtonWasPressed(2))
    print('-'*5+'trying out macro off command'+'-'*50)
    print(remote.offButtonWasPressed(2))
    print('-'*5+'trying out macro undo command'+'-'*50)
    print(remote.undoButtonWasPressed())
