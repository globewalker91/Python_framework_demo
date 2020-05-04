import pytest
import unittest


class TestAbsoluteSorting(unittest.TestCase):
    @staticmethod
    def checkio(numbers_array: tuple) -> list:
        """
        helper function used returns ints sorted by abs value

        sample usage:
        print(self.checkio((-20, -5, 10, 15)))
        print(self.checkio((1, 2, 3, 0)))
        print(self.checkio((-1, -2, -3, 0)))

        """
        return sorted(numbers_array, key=abs)

    def test_checkio(self):
        self.assertEqual(self.checkio((-20, -5, 10, 15)), [-5, 10, 15, -20])
        self.assertEqual(self.checkio((1, 2, 3, 0)), [0, 1, 2, 3])
        self.assertEqual(self.checkio((-1, -2, -3, 0)), [0, -1, -2, -3])

    def test_intentional_fail_4(self):
        self.assertTrue(False)

    @pytest.mark.xfail
    def test_fail_expected(self):
        self.assertTrue(False)

    @pytest.mark.skip
    def test_skip(self):
        self.assertTrue(False)
