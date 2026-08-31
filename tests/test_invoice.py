from calc.invoice import subtotal, invoice_total


def test_subtotal():
    assert subtotal([10, 20, 30]) == 60


def test_invoice_total_no_discount():
    assert invoice_total([10, 20, 30]) == 60


def test_invoice_total_with_discount():
    assert invoice_total([100.0], 10) == 90.0
