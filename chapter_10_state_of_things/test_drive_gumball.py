from simple_gumball_machine import GumballMachine

if __name__=='__main__':
    gumball_machine=GumballMachine(2)

    gumball_machine.turnCrank()
    gumball_machine.insertQuarter()
    gumball_machine.turnCrank()
    gumball_machine.ejectQuarter()
    gumball_machine.insertQuarter()
    gumball_machine.ejectQuarter()
    gumball_machine.insertQuarter()
    gumball_machine.turnCrank()
    gumball_machine.insertQuarter()
    gumball_machine.turnCrank()
