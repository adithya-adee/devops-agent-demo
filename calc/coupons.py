import os
import ast
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

def _safe_eval(expr):
    """
    Safely evaluate a simple arithmetic expression containing only numbers and
    the operators +, -, *, /, and parentheses.
    """
    node = ast.parse(expr, mode='eval')
    for subnode in ast.walk(node):
        if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp,
                                    ast.Num, ast.Constant,
                                    ast.operator, ast.unaryop)):
            raise ValueError("Invalid coupon code")
    return eval(compile(node, '<string>', 'eval'), {}, {})
def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    pct = _safe_eval(code)
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return password == ADMIN_PASSWORD
