import pytest

def first_word(text):
    import re
    edit1 = text.replace(",", "")
    edit2 = edit1.replace(".", " ")
    edit3 = edit2.strip()
    split_list = edit3.split(" ")
    return split_list[0]
 
def test_first_word():
    assert first_word("Hello world") == 'Hello'
    assert first_word("greetings, friends") == 'greetings'
    assert first_word(" a word ") == 'a'
    assert first_word("Hello.world") == 'Hello'

def test_intentional_fail():
    assert True == False
