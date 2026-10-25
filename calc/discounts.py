"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price - price * (pct / 100)  # demo 03:34:40: BUG — should subtract
