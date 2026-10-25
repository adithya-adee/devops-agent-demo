"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price + price * (pct / 100)  # demo 04:45:43: BUG — should subtract
