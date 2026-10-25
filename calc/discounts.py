"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price - price * (pct / 100)  # corrected: applies discount by subtraction
