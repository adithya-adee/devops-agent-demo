"""Currency rounding helpers."""

from decimal import Decimal, ROUND_HALF_UP


def round_currency(amount):
    """Round `amount` to 2 decimal places using half-up rounding."""
    return float(Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
