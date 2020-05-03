import pytest

def days_diff(a, b):
    import datetime

    date_a = datetime.date(a[0], a[1], a[2])
    date_b = datetime.date(b[0], b[1], b[2])
    # your code here
    return abs((date_b - date_a).days)



    # These "asserts" are used for self-checking and not for an auto-testing
""" print(days_diff((1982, 4, 19), (1982, 4, 22))) == 3
print(days_diff((2014, 1, 1), (2014, 8, 27)))  == 238
print(days_diff((2014, 8, 27), (2014, 1, 1))) == 238 """

def test_days_diff():
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27))  == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

def test_intentional_fail_2():
    assert True == False
