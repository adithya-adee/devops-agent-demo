"""Sales-tax helpers."""

TAX_RATE = 0.10


def apply_tax(amount):
    """Return `amount` with sales tax added."""
    return amount + amount * TAX_RATE
