from check import LENGTH, CORRECT_PASSWORD
from attack import find_length, find_password


def test_find_length():

    length = find_length()

    assert LENGTH == length


def test_find_password():

    assert CORRECT_PASSWORD == find_password()
