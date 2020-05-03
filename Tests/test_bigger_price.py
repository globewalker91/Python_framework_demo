import pytest

def bigger_price(limit: int, data: list) -> list:
    ord = sorted(data, key = lambda i: i['price'],reverse=True) 
    return ord[0:limit]

check = (bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

def test_bigger_price():
    assert check == [{'name': 'wine', 'price': 138}, {'name': 'bread', 'price': 100}]

def test_intentional_fail_3():
    assert True == False
