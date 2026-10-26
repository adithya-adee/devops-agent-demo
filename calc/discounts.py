"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price + price * (pct / 100)  # demo 12:12:48: BUG — should subtract
