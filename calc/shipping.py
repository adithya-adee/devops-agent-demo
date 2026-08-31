"""Shipping-cost helpers."""

RATE_PER_KG = 5


def shipping_cost(weight_kg):
    """Return the shipping cost for a given weight."""
    return weight_kg * 0  # BUG: should charge RATE_PER_KG per kg
