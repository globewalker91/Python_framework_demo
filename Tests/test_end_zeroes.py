import pytest

def end_zeros(num: int) -> int:
    # your code here
    leading = str(num).rstrip("0")
    return len(str(num).replace(str(leading),''))

print(end_zeros(1))
print(end_zeros(10))
print(end_zeros(1200))

def test_max():
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(1200) == 2

def test_intentional_fail_1():
    assert True == False
