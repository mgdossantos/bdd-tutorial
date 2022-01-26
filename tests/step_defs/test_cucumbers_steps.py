from pytest_bdd import scenarios, parsers, given, when, then
from cucumbers import CucumberBasket

CONVERTERS={
    'initial':int,
    'some':int,
    'total':int,
}

EXTRA_TYPES={
    'Number':int,
}

scenarios('../features/cucumbers.feature')


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
@given('the basket has "<initial>" cucumbers', target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket,some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket,some):
    basket.remove(some)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket,total):
    assert basket.count == total
