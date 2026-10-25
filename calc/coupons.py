import os

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    pct = eval(code, {"__builtins__": None}, {})
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return password == ADMIN_PASSWORD
