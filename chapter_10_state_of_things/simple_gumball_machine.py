class GumballMachine():
    SOLD_OUT=0
    NO_QUARTER=1
    HAS_QUARTER=2
    SOLD=3
    
    def __init__(self,count):
        
        
        self.state=self.SOLD_OUT

        self.count=count
        if self.count>0:
            self.state=self.NO_QUARTER

    def insertQuarter(self):
        if self.state==self.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state==self.NO_QUARTER:
            self.state=self.HAS_QUARTER
            print('You have inserted a quarter')
        elif self.state==self.SOLD_OUT:
            print('You cant insert a quareter the machine is sold out')
        elif self.state==self.SOLD:
            print()
    
    def turnCrank(self):
        if self.state==self.HAS_QUARTER:
            self.state=self.SOLD
            self.dispense()
            print("Rolling out a gumball")
        elif self.state==self.NO_QUARTER:
            print('You have to insert a quarter first')
        elif self.state==self.SOLD_OUT:
            print('You cant the machine is sold out')
        elif self.state==self.SOLD:
            print('We are already providing you a gumball')

    def ejectQuarter(self):
        if self.state==self.HAS_QUARTER:
            self.state=self.NO_QUARTER
            print("Your Quarter Returned")
        elif self.state==self.NO_QUARTER:
            print('You have to insert a quarter first')
        elif self.state==self.SOLD_OUT:
            print('You cant, you havent inserted a quarter yet')
        elif self.state==self.SOLD:
            print('We are already providing you a gumball')

    def dispense(self):
        if self.state==self.HAS_QUARTER:
            print("Your Need to turn the crank first")
        elif self.state==self.NO_QUARTER:
            print('You have to insert a quarter first')
        elif self.state==self.SOLD_OUT:
            print('No Gumball dispensed')
        elif self.state==self.SOLD:
            print('A gumball rolling out')
            self.count-=1
            if self.count==0:
                self.state=self.SOLD_OUT
            else:
                self.state=self.NO_QUARTER
        
