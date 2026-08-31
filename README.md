# billing-demo

A tiny billing package used to demo an autonomous CI-fix agent. Each module is
independent (low cross-file coupling), so a fix touches only the files that are wrong:

- `calc/operations.py` — `add`, `multiply`
- `calc/discounts.py` — `apply_discount`
- `calc/tax.py` — `apply_tax`
- `calc/shipping.py` — `shipping_cost`
- `tests/test_billing.py` — one test per module
