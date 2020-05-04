import pytest
from typing import Iterable

def replace_first(items: list) -> Iterable:
    if len(items) <= 1:
        return items
    else:
        first = items[0]
        items.append(first)
        del items[0]
        return items

print(replace_first([1, 2, 3, 4]))
print(replace_first([1]))
print(replace_first([]))

def test_max():
    assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert replace_first([1]) == [1]
    assert replace_first([]) == []

def test_intentional_fail_3():
    assert True == False