import pytest

def max_digit(number: int) -> int:
    res = [int(x) for x in str(number)] 
    return max(res)

print(max_digit(0))
print(max_digit(52))
print(max_digit(634))
print(max_digit(1))
print(max_digit(10000))

def test_max():
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1

def test_intentional_fail_5():
    assert True == False
