from SimUDucks import (Quackable, MallardDuck,RubberDuck,DuckWistle,Goose,
                       DuckAdapter,QuackCounter,CounterDuckFactory,NormalDuckFactory,
                       Flock,Observer,Observable,QuackObservable)
import pytest

@pytest.fixture(autouse=True)
def reset_quack_count():
    """Reset quack count before each test"""
    QuackCounter.count=0
    yield

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
    assert QuackCounter.getCount()==4


def test_duck_factory_method_for_creating_different_families_of_ducks():
    counter_duck_factory=CounterDuckFactory()
    normal_duck_factory=NormalDuckFactory()

    counter_mallard_duck=counter_duck_factory.createMallardDuck()
    normal_mallard_duck=normal_duck_factory.createMallardDuck()
    counter_goose_duck=counter_duck_factory.createDuckAdapter()


    counter_mallard_duck.quack()
    counter_mallard_duck.quack()
    counter_mallard_duck.quack()
    counter_goose_duck.quack()
    
    

    assert normal_mallard_duck.quack()=='Quack'
    assert counter_goose_duck.quack()=="Honk"
    assert QuackCounter.getCount()==5
    


def test_flock_works_by_calling_all_birds_in_flock():
    counter_duck_factory=CounterDuckFactory()
    normal_duck_factory=NormalDuckFactory()

    counter_mallard_duck=counter_duck_factory.createMallardDuck()
    normal_mallard_duck=normal_duck_factory.createMallardDuck()
    counter_goose_duck=counter_duck_factory.createDuckAdapter()
    mallard_duck_1=counter_duck_factory.createMallardDuck()
    mallard_duck_2=counter_duck_factory.createMallardDuck()
    mallard_duck_3=counter_duck_factory.createMallardDuck()

    flock=Flock([counter_mallard_duck,normal_mallard_duck,counter_goose_duck,])
    flockOFMallards=Flock()
    flockOFMallards.add(mallard_duck_1)
    flockOFMallards.add(mallard_duck_2)
    flockOFMallards.add(mallard_duck_3)
    flock.add(flockOFMallards)

    flock.quack()
    
    

    assert normal_mallard_duck.quack()=='Quack'
    assert counter_goose_duck.quack()=="Honk"
    assert QuackCounter.getCount()==6




def test_quackologists_able_to_observe_duck_quack(capsys):

    normal_duck_factory=NormalDuckFactory()
    counter_duck_factory=CounterDuckFactory()
    counterMallard_duck=normal_duck_factory.createMallardDuck()
    
    quackologist=Observer('Quackologist_jim')
    counterMallard_duck.add_observer(quackologist)

    print(counterMallard_duck.quack())

    captured=capsys.readouterr()
    assert captured.out=="Quackologist_jim observed a Quack \nQuack\n"