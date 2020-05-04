import datetime
import unittest


class TestDaysBetween(unittest.TestCase):
    @staticmethod
    def days_diff(a, b):
        """
        helper function returns the date in days given a datetime.date object

        sample usage:
        print(days_diff((1982, 4, 19), (1982, 4, 22))) == 3
        print(days_diff((2014, 1, 1), (2014, 8, 27)))  == 238
        print(days_diff((2014, 8, 27), (2014, 1, 1))) == 238

        """
        date_a = datetime.date(a[0], a[1], a[2])
        date_b = datetime.date(b[0], b[1], b[2])
        return abs((date_b - date_a).days)

    def test_days_diff(self):
        self.assertEqual(self.days_diff((1982, 4, 19), (1982, 4, 22)), 3)
        self.assertEqual(self.days_diff((2014, 1, 1), (2014, 8, 27)), 238)
        self.assertEqual(self.days_diff((2014, 8, 27), (2014, 1, 1)), 238)

    def test_intentional_fail_2(self):
        self.assertTrue(False)
