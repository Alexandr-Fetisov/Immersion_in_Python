from script_6_7 import is_real_date
from script_6_7 import is_leap_year
import script_5_9_DZ
import unittest


class TestCalendar(unittest.TestCase):
    def test_add(self):
        date = "11.5.1995"
        self.assertEqual(date, '11.5.1995')

    def test_real(self):
        date = "11.5.1995"
        self.assertTrue(is_real_date(date))

    def test_is_leap_year1(self):
        self.assertTrue(is_leap_year(2004))

    def test_is_leap_year(self):
        self.assertFalse(is_leap_year(2200))


class TestDict(unittest.TestCase):
    def test_dict(self):
        names = ['Виктор', 'Михаил', 'Аня']
        rate = [80000, 100000, 90000]
        bonus = ["10%", "12%", "10%"]
        dict_res = script_5_9_DZ.bonus(names, rate, bonus, 3)
        self.assertEqual(dict_res, {'Виктор': 8000.0, 'Михаил': 12000.0, 'Аня': 9000.0})


if __name__ == '__main__':
    unittest.main()
