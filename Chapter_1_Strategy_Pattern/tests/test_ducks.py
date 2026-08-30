from ducks import Duck,Quack,Squeal,NoQuack,FlyWithWings,FlyNoWay,FlyBehaviour,QuackBehaviour

def test_mallard_duck_behaviour():
    mallard_duck=Duck(FlyWithWings(),Quack(),)

    assert mallard_duck.quack()=='this duck quacks'
    assert mallard_duck.fly()=='this duck flies with wings'
    assert mallard_duck.swim()=='this duck can swim'

def test_rubbar_duck_behaviour():
    rubber_duck=Duck(FlyNoWay(),Squeal())

    assert rubber_duck.quack()=='this duck squeals'
    assert rubber_duck.fly()=='this duck does not fly'
    assert rubber_duck.swim()=='this duck can swim'

def test_wooden_duck_behaviour():
    wooden_duck=Duck(FlyNoWay(),NoQuack(),)

    assert wooden_duck.quack()=='this duck does not quack'
    assert wooden_duck.fly()=='this duck does not fly'
    assert wooden_duck.swim()=='this duck can swim'


def test_dynamic_change_custom_setter_duck_behaviour():
    custom_duck=Duck(quack_behaviour=Squeal())

    assert custom_duck.quack()=='this duck squeals'

    custom_duck.set_fly_behaviour(FlyWithWings())
    custom_duck.set_quack_behaviour(NoQuack())

    assert custom_duck.quack()=='this duck does not quack'
    assert custom_duck.fly()=='this duck flies with wings'
    assert custom_duck.swim()=='this duck can swim'



