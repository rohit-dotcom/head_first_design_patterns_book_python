from turkey_adapter import MallardDuck,Turkey,turkeyAdapter,Duck


def test_mallard_duck_quakck_and_flies():
    mal_duck=MallardDuck('Mal')
    assert mal_duck.quack()=='This Mallard Duck Quacks'
    assert mal_duck.fly()=="This Mallard Duck Flys"

def test_turkey_gobbles_and_flies_short_distances():
    turk=Turkey('Turkiye')
    assert turk.gobble()=='this turkey gobbles'
    assert turk.fly_short_distance()=='this turkey flies short distance'

def test_turkey_adapter_can_call_quack_for_turkey():
    turk=Turkey('fake_turkey')
    adapter=turkeyAdapter(turk)
    assert adapter.quack()=='this turkey gobbles'
    # assert adapter.fly()=='this turkey flys'