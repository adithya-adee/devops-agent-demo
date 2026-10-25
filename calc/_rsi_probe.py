"""RSI delta-update probe — added and removed again by scripts/e2e.py."""

from calc.operations import add


def rsi_probe_total(items):
    """Sum `items` using calc.operations.add."""
    total = 0
    for item in items:
        total = add(total, item)
    return total
