from gumball_machine_with_states import Gumball_Machine


if __name__=='__main__':
    gumball_machine=Gumball_Machine(5)
    gumball_machine.insertQuarter()
    gumball_machine.turnCrank()
    gumball_machine.ejectQuarter()
    gumball_machine.turnCrank()
    gumball_machine.insertQuarter()
    gumball_machine.turnCrank()