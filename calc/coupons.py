import os, ast, operator

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def apply_coupon(price, code):
    # coupon codes are math expressions sent by the client, e.g. "5*2"
    pct = _safe_eval(code)
    return price - price * pct / 100
def _safe_eval(expr):
    import ast as _ast
    import operator as _op
    allowed_operators = {
        _ast.Add: _op.add,
        _ast.Sub: _op.sub,
        _ast.Mult: _op.mul,
        _ast.Div: _op.truediv,
        _ast.Mod: _op.mod,
        _ast.Pow: _op.pow,
        _ast.USub: _op.neg,
    }

    def _eval(node):
        if isinstance(node, _ast.Num):
            return node.n
        if isinstance(node, _ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid constant")
        if isinstance(node, _ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            raise ValueError("Unsupported operator")
        if isinstance(node, _ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            raise ValueError("Unsupported unary operator")
        raise ValueError("Unsupported expression")

    node = _ast.parse(expr, mode='eval')
    return _eval(node.body)

def load_coupons(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_admin(password):
    return password == ADMIN_PASSWORD
