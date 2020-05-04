from typing import Iterable
import unittest


class TestReplaceFirst(unittest.TestCase):
    @staticmethod
    def replace_first(items: list) -> Iterable:
        """
        sample usage:
        print(TestReplaceFirst.replace_first([1, 2, 3, 4]))
        print(TestReplaceFirst.replace_first([1]))
        print(TestReplaceFirst.replace_first([]))

        """
        if len(items) <= 1:
            return items
        else:
            first = items[0]
            items.append(first)
            del items[0]
        return items

    def test_max(self):
        """Validates that the first item is moved to the end"""
        self.assertEqual(self.replace_first([1, 2, 3, 4]), [2, 3, 4, 1])
        self.assertEqual(self.replace_first([1]), [1])
        self.assertEqual(self.replace_first([]), [])

    def test_intentional_fail_3(self):
        self.assertTrue(False)
