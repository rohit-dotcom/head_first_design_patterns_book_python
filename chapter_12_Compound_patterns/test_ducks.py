from SimUDucks import Quackable, MallardDuck,RubberDuck,DuckWistle,Goose,DuckAdapter,QuackCounter

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

def test_decorator_is_able_to_add_count_functionality_to_any_duck():
    duck=MallardDuck()
    goose=Goose()
    adapter=DuckAdapter(goose)

    quack_counter_1=QuackCounter(duck)
    quack_counter_2=QuackCounter(adapter)

    quack_counter_1.quack()
    quack_counter_2.quack()
    quack_counter_2.quack()

    assert quack_counter_2.quack()=="Honk"
    assert quack_counter_2.getCount()==4
    assert quack_counter_1.getCount()==4
