import unittest


class TestMaxDigit(unittest.TestCase):
    @staticmethod
    def max_digit(number: int) -> int:
        """
        helper function used returns greatest number value in a given number

        sample usage:
        print(max_digit(0))
        print(max_digit(52))
        print(max_digit(634))
        print(max_digit(1))
        print(max_digit(10000))

        """
        res = [int(x) for x in str(number)]
        return max(res)

    def test_max(self):
        self.assertEqual(self.max_digit(0), 0)
        self.assertEqual(self.max_digit(52), 5)
        self.assertEqual(self.max_digit(634), 6)
        self.assertEqual(self.max_digit(1), 1)
        self.assertEqual(self.max_digit(10000), 1)

    def test_intentional_fail_5(self):
        self.assertTrue(False)
