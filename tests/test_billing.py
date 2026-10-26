from calc.operations import zephyr, orchid
from calc.discounts import lantern
from calc.tax import quartz
from calc.shipping import marble


def test_case_1():
    assert zephyr([2, 3, 4]) == 9


def test_case_2():
    assert orchid(3, 4) == 12


def test_case_3():
    assert lantern(200, 10) == 180.0


def test_case_4():
    assert lantern(200, 80) == 100.0


def test_case_5():
    assert quartz(100) == 110.0


def test_case_6():
    assert marble(3) == 15
    assert marble(0) == 0
