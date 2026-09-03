from coffees import Expresso,Whip,House_Blend,Soy

def test_subclasses_able_to_instantiate():
    house_blend=House_Blend()

    assert house_blend.get_description()=='House Blend'
    assert house_blend.cost()==0.89

def test_decorator_able_to_use_superclass_and_subclasses():
    new_expresso=Expresso()
    new_expresso=Whip(new_expresso)

    assert new_expresso.get_description()=='Expresso, whip'
    assert new_expresso.cost()==2.09

def test_house_blend_with_soy():
    hb=House_Blend()
    hb=Soy(hb)

    assert hb.get_description()=='House Blend, soy'
    assert hb.cost()==1.04


def test_able_to_wrap_2_condiments_to_one_coffee():
    house_blend=House_Blend()
    house_blend=Whip(house_blend)
    house_blend=Soy(house_blend)

    assert house_blend.get_description()=='House Blend, whip, soy'
    assert house_blend.cost()==1.14


def test_expresso_with_double_whip():
    ex=Expresso()
    ex=Whip(ex)
    ex=Whip(ex)

    assert ex.get_description()=='Expresso, whip, whip'
    assert ex.cost()==2.19