from pizzas import Pizza,PepperoniPizza,CheesePizza,veggiePizza,PizzaStore,NYPizzaStore,ChicagoPizzaStore,NY_ingredients_factory

def test_able_to_create_instances_of_differen_pizzas():

    cheese_pizza=CheesePizza()
    pep_piz=PepperoniPizza()
    veg_piz=veggiePizza()

    assert cheese_pizza.bake()=='Baking cheese pizza!'
    assert pep_piz.cut()=='Cutting in diagonal pieces'
    assert veg_piz.box()=='Boxing veggie pizza'

def test_order_pizza_is_able_return_pizza_from_NY_Pizza_store():
    pizza_store=NYPizzaStore()
    pizza=pizza_store.orderPizza('veggie')
    assert pizza.box()=='Boxing NYveggie pizza'

def test_order_pizza_is_able_return_pizza_from_chicago_Pizza_store():
    pizza_store=ChicagoPizzaStore()
    pizza=pizza_store.orderPizza('veggie')
    assert pizza.box()=='Boxing Chichago veggie pizza'

def test_if_ingredient_factory_is_able_to_pass_on_ingredients_to_store():

    ingredient_factory=NY_ingredients_factory()
    pizza_store=NYPizzaStore(ingredient_factory)
    pizza=pizza_store.orderPizza('veggie')
    assert pizza.box()=='Boxing BYveggie pizza'

