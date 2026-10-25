"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price + price * (pct / 100)  # demo 19:07:24: BUG — should subtract
