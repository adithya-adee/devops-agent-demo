import os
import ast

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
if ADMIN_PASSWORD is None:
    raise RuntimeError("ADMIN_PASSWORD not set")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    # Safely evaluate arithmetic expression for percentage
    try:
        node = ast.parse(code, mode='eval')
        for subnode in ast.walk(node):
            if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant, ast.operator)):
                raise ValueError("Invalid coupon code")
        pct = eval(compile(node, '<string>', 'eval'))
    except Exception as e:
        raise ValueError("Invalid coupon code") from e
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return password == ADMIN_PASSWORD
