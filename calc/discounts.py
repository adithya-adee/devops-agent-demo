"""Discount helpers."""


def apply_discount(price, pct):
    """Return `price` after applying a `pct` percent discount."""
    return price + price * (pct / 100)  # demo 15:04:05: BUG — should subtract
