import os
import ast
import operator
import hmac
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
def _safe_eval(expr):
    """
    Safely evaluate a simple arithmetic expression containing numbers and
    the operators +, -, *, /, **, and parentheses.
    """
    allowed_nodes = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd,
        ast.Load, ast.Mod, ast.FloorDiv, ast.LParen, ast.RParen
    }
    node = ast.parse(expr, mode='eval')
    for subnode in ast.walk(node):
        if not isinstance(subnode, tuple(allowed_nodes)):
            raise ValueError("Invalid expression")
    return eval(compile(node, filename="<ast>", mode="eval"), {"__builtins__": {}}, {})    pct = _safe_eval(code)
    return price - price * pct / 100


def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return hmac.compare_digest(password, ADMIN_PASSWORD or "")
