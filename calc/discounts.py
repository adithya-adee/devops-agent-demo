"""Discount helpers, built on the core operations."""
from calc.operations import multiply


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    reduction = multiply(price, pct / 100)
    return price - reduction
