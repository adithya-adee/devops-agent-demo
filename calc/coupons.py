import os
import ast
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    try:
        node = ast.parse(code, mode='eval')
        allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant, ast.operator, ast.unaryop)
        if not all(isinstance(n, allowed) for n in ast.walk(node)):
            raise ValueError("Invalid coupon expression")
        pct = eval(compile(node, '<string>', 'eval'))
    except Exception:
        raise ValueError("Invalid coupon code")
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return password == ADMIN_PASSWORD
