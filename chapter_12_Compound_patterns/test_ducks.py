from SimUDucks import Quackable, MallardDuck,RubberDuck,DuckWistle,Goose,DuckAdapter

def test_quackable_ducks_can_quack():
    mallard_duck=MallardDuck()
    rubber_duck=RubberDuck()
    duck_wistle=DuckWistle()

    assert mallard_duck.quack()=='Quack'
    assert rubber_duck.quack()=='Squeak'
    assert duck_wistle.quack()=='Kwaq'

def test_duck_adapter_is_able_to_adapt_goose():
    goose=Goose()
    duck_adapted_goose=DuckAdapter(goose)

    assert goose.honk()=="Honk"
    assert duck_adapted_goose.quack()=="Honk"