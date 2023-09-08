"""
Test goes here

"""

from main import add


def test_add_positive_numbers():
    assert add(3, 5) == 8


def test_add_negative_numbers():
    assert add(-3, -5) == -8


def test_add_mixed_numbers():
    assert add(3, -5) == -2


if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    print("All tests passed.")
