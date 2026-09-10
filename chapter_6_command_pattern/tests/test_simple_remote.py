from simple_remote import simpleRemote,LightOnCommand,Light

def test_able_to_set_and_execute_light_on_command():
    light1=Light()
    command=LightOnCommand(light1)
    remote=simpleRemote()
    remote.set_command(command)

    assert remote.button_pressed()=='This light is on!'