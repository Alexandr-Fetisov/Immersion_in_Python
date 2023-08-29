from script_6_7 import is_real_date
from script_6_7 import is_leap_year
import script_5_9_DZ


def test_add():
    """
    >>> date="11.5.1995"
    >>> date
    '11.5.1995'

    >>> is_real_date(date)
    True

    >>> is_leap_year(2004)
    True

    >>> is_leap_year(2200)
    False
    """


def test_dict():
    """
    >>> names=['Виктор', 'Михаил', 'Аня']
    >>> rate=[80000, 100000, 90000]
    >>> bonus = ["10%", "12%", "10%"]
    >>> script_5_9_DZ.bonus(names,rate,bonus,3)
    {'Виктор': 8000.0, 'Михаил': 12000.0, 'Аня': 9000.0}

    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
