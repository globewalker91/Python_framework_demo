import pytest

def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key = abs)

print(checkio((-20, -5, 10, 15)))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))

def test_checkio():
    assert checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20]
    assert checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
    assert checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]

def test_intentional_fail_4():
    assert True == False

@pytest.mark.xfail
def test_fail_expected():
    assert True == False

@pytest.mark.skip
def test_skip():
    assert True == False

