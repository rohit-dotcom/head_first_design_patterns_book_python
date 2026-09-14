class Duck():
    def __init__(self,name:str,height:int,age:int):
        self.name=name
        self.height=height
        self.age=age

    def __repr__(self):
        return self.name

def compare_duck_age(duck1:Duck,duck2:Duck):
    if duck1.age>duck2.age:
        return -1
    elif duck1.age<duck2.age:
        return 1
    else:
        return 0
def compare_duck_height(duck1:Duck,duck2:Duck):
    if duck1.height>duck2.height:
        return -1
    elif duck1.height<duck2.height:
        return 1
    else:
        return 0
