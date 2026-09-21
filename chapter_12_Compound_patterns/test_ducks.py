from SimUDucks import Quackable, MallardDuck,RubberDuck,DuckWistle

def test_quackable_ducks_can_quack():
    mallard_duck=MallardDuck()
    rubber_duck=RubberDuck()
    duck_wistle=DuckWistle()

    assert mallard_duck.quack()=='Quack'
    assert rubber_duck.quack()=='Squeak'
    assert duck_wistle.quack()=='Kwaq'

