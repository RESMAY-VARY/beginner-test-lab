import pytest
from buggy_script import add_numbers, get_first_item, divide, format_name

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_get_first_item():
    assert get_first_item([10, 20, 30]) == 10

def test_divide():
    assert divide(10, 2) == 5

def test_format_name():
    assert format_name("laura", "smith") == "laura SMITH"

