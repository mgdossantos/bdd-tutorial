from pytest_bdd import scenarios, parsers, given, when, then
from cucumbers import CucumberBasket

scenarios('../features/cucumbers.feature')

# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
# def test_add():
#     pass

# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
# def test_remove():
#     pass

EXTRA_TYPES={
    'Number':int,
}

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
#@given("the basket has 2 cucumbers",target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)
    #return CucumberBasket(initial_count=2)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
#@when("4 cucumbers are added to the basket")
def add_cucumbers(basket,some):
#def add_cucumbers(basket):
    basket.add(some)
    #basket.add(4)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
#@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=dict(Number=int)))
#@when("4 cucumbers are added to the basket")
def remove_cucumbers(basket,some):
#def add_cucumbers(basket):
    basket.remove(some)
    #basket.add(4)



@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
def basket_has_total(basket,total):
    assert basket.count == total
