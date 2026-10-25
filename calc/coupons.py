import os
import hmac
import ast
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    node = ast.parse(code, mode='eval')
    for subnode in ast.walk(node):
        if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant, ast.operator, ast.unaryop)):
            raise ValueError("Invalid coupon expression")
    pct = eval(compile(node, '<string>', 'eval'))
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    if not ADMIN_PASSWORD:
        return False
    return hmac.compare_digest(password, ADMIN_PASSWORD)
