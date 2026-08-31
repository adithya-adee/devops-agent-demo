# billing-demo

A tiny billing package used to demo an autonomous CI-fix agent.

- `calc/operations.py` — core arithmetic (`add`, `subtract`, `multiply`)
- `calc/discounts.py` — `apply_discount`, built on `operations`
- `calc/invoice.py` — `subtotal`, `invoice_total`, built on `operations` + `discounts`
- `tests/` — pytest suite run in CI

A bug in the shared `operations.add` cascades into the invoice tests.
