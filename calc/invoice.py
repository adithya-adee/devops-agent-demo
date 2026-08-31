"""Invoice calculations, built on operations and discounts."""
from calc.operations import add
from calc.discounts import apply_discount


def subtotal(prices):
    """Sum all line-item prices using the core add() operation."""
    total = 0
    for price in prices:
        total = add(total, price)
    return total


def invoice_total(prices, discount_pct=0):
    """Return the invoice subtotal after an optional percentage discount."""
    return apply_discount(subtotal(prices), discount_pct)
