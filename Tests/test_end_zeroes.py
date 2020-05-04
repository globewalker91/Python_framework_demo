import unittest


class TestEndZeros(unittest.TestCase):
    @staticmethod
    def end_zeros(num: int) -> int:
        """
        helper function strips trailing zeros

        sample usage:
        print(end_zeros(1))
        print(end_zeros(10))
        print(end_zeros(1200))

        """
        leading = str(num).rstrip("0")
        return len(str(num).replace(str(leading), ''))

    def test_max(self):
        self.assertEqual(self.end_zeros(1), 0)
        self.assertEqual(self.end_zeros(10), 1)
        self.assertEqual(self.end_zeros(1200), 2)

    def test_intentional_fail_1(self):
        self.assertTrue(False)
