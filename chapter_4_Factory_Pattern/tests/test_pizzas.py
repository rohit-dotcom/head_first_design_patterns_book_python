from pizzas import Pizza,PepperoniPizza,CheesePizza,veggiePizza,simplePizzaFactory,PizzaStore

def test_able_to_create_instances_of_differen_pizzas():

    cheese_pizza=CheesePizza()
    pep_piz=PepperoniPizza()
    veg_piz=veggiePizza()

    assert cheese_pizza.bake()=='Baking cheese pizza!'
    assert pep_piz.cut()=='Cutting in diagonal pieces'
    assert veg_piz.box()=='Boxing veggie pizza'

def test_order_pizza_is_able_return_pizza():
    factory=simplePizzaFactory()
    pizza_store=PizzaStore(factory)
    pizza=pizza_store.orderPizza('veggie')
    assert pizza.box()=='Boxing veggie pizza'



