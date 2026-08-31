from calc.operations import add
from calc.discounts import apply_discount
from calc.tax import apply_tax
from calc.shipping import shipping_cost


def test_add():
    assert add(2, 3) == 5


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_apply_tax():
    assert apply_tax(100) == 110


def test_shipping_cost():
    assert shipping_cost(3) == 15
