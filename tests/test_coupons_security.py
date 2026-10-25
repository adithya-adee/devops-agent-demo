"""Security checks for the coupons fix (added by scripts/e2e.py)."""
import pytest

from calc import coupons
from calc.coupons import apply_coupon, is_admin


def test_coupon_math_still_works():
    # Contract from the original code: codes are arithmetic expressions
    assert apply_coupon(100, "5*2") == 90
    assert apply_coupon(100, "10") == 90


@pytest.mark.parametrize("payload", [
    "__import__('os').getcwd() and 10",
    # escapes eval(code, {"__builtins__": None}, {}) — no builtins needed
    "().__class__.__base__.__subclasses__() and 10",
    "(lambda: 10)()",
    "[x for x in (10,)][0]",
])
def test_coupon_does_not_run_code(payload):
    # Refusing (raise) or ignoring the code is fine; evaluating it (10% off) is not
    try:
        result = apply_coupon(100, payload)
    except Exception:
        return
    assert result != 90, f"coupon code was executed: {payload!r}"


def test_is_admin_checks_the_password(monkeypatch):
    monkeypatch.setenv("ADMIN_PASSWORD", "s3cret")
    monkeypatch.setattr(coupons, "ADMIN_PASSWORD", "s3cret", raising=False)
    assert is_admin("wrong") is False
    assert is_admin("s3cret") is True


def test_is_admin_fails_closed_without_a_password(monkeypatch):
    # With no password configured nobody is admin — not even `None == None`
    monkeypatch.delenv("ADMIN_PASSWORD", raising=False)
    monkeypatch.setattr(coupons, "ADMIN_PASSWORD", None, raising=False)
    assert not is_admin(None)
    assert not is_admin("")
