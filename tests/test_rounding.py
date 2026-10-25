from calc.rounding import round_currency


def test_round_currency():
    assert round_currency(2.675) == 2.68
    assert round_currency(10) == 10.0
