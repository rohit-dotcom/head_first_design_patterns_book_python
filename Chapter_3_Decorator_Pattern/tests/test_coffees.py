from coffees import Expresso,Whip,House_Blend,Soy

def test_subclasses_able_to_instantiate():
    house_blend=House_Blend()

    assert house_blend.get_description()=='House Blend'
    assert house_blend.cost()==0.89

def test_decorator_able_to_use_superclass_and_subclasses():
    new_expresso=Expresso()
    expresso_with_whip=Whip(new_expresso)

    assert expresso_with_whip.get_description()=='Expresso, whip'
    assert expresso_with_whip.cost()==2.09

def test_house_blend_with_soy():
    hb=House_Blend()
    hb_with_whip=Soy(hb)

    assert hb_with_whip.get_description()=='House Blend, soy'
    assert hb_with_whip.cost()==1.04


def test_able_to_wrap_2_condiments_to_one_coffee():
    house_blend=House_Blend()
    house_blend_with_whip=Whip(house_blend)
    house_blend_with_whip_and_soy=Soy(house_blend_with_whip)

    assert house_blend_with_whip_and_soy.get_description()=='House Blend, whip, soy'
    assert house_blend_with_whip_and_soy.cost()==1.14


def test_expresso_with_double_whip():
    ex=Expresso()
    ex_wp=Whip(ex)
    ex_wp_wp=Whip(ex_wp)

    assert ex_wp_wp.get_description()=='Expresso, whip, whip'
    assert ex_wp_wp.cost()==2.19