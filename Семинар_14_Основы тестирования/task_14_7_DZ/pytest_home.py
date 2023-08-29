from script_6_7 import is_real_date
from script_6_7 import is_leap_year
import script_5_9_DZ
import pytest


def test_add():
    date = "11.5.1995"
    assert date == '11.5.1995'


def test_real():
    date = "11.5.1995"
    assert is_real_date(date) == True


def test_is_leap_year1():
    assert is_leap_year(2004) == True


def test_is_leap_year():
    assert is_leap_year(2200) == False


def test_dict():
    names = ['Виктор', 'Михаил', 'Аня']
    rate = [80000, 100000, 90000]
    bonus = ["10%", "12%", "10%"]
    assert (script_5_9_DZ.bonus(names, rate, bonus, 3), {'Виктор': 8000.0, 'Михаил': 12000.0, 'Аня': 9000.0})


if __name__ == '__main__':
    pytest.main()
