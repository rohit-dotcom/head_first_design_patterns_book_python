from simple_remote import simpleRemote,LightOnCommand,Light,GarageDoor,GaragerDoorOpenCommand

def test_able_to_set_and_execute_light_on_command():
    light1=Light()
    command=LightOnCommand(light1)
    remote=simpleRemote()
    remote.set_command(command)

    assert remote.button_pressed()=='This light is on!'


def test_able_to_set_and_execute_light_and_garage_door_on_command():
    light1=Light()
    command1=LightOnCommand(light1)
    remote=simpleRemote()
    remote.set_command(command1)

    assert remote.button_pressed()=='This light is on!'
    garage_door=GarageDoor()
    command2=GaragerDoorOpenCommand(garage_door)
    remote.set_command(command2)
    
    assert remote.button_pressed()=='This Garage Door is opened!'