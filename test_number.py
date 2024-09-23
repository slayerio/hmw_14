from get_number import check_guess  # Import only the function you want to test
import pytest


def test_bingo():
    expected = "BINGO!"
    actual = check_guess(50, "50")
    print(f"Expected: {expected}, Actual: {actual}")
    assert expected == actual


def test_invalid_number():
    with pytest.raises(ValueError):
        check_guess(50, "fort")


def test_out_of_range_positive():
    with pytest.raises(ValueError) as ex:
        check_guess(50, "138")
    assert str(ex.value) == "Number out of range"


def test_negative():
    with pytest.raises(ValueError) as ex:
        check_guess(50, "-50")
    assert str(ex.value) == "Number is negative"


def test_higher():
    expected = "higher"
    actual = check_guess(50, "40")
    print(f"Expected: {expected}, Actual: {actual}")
    assert expected == actual


def test_lower():
    expected = "lower"
    actual = check_guess(50, "60")
    print(f"Expected: {expected}, Actual: {actual}")
    assert expected == actual
