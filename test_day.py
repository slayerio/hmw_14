from get_day import check_number
import pytest


def zero_negative():
    expected = "number cannot be zero or negative"
    actual = check_number(0)
    assert expected == actual


def out_of_range():
    expected = "number is out of range"
    actual = check_number(9)
    assert expected == actual


def invalid_number():
    with pytest.raises(ValueError):
        check_number("sunday")



def test_day1():
    expected = "sunday"
    actual = check_number(1)
    assert expected == actual


def test_day2():
    expected = "monday"
    actual = check_number(2)
    assert expected == actual


def test_day3():
    expected = "tuesday"
    actual = check_number(3)
    assert expected == actual


def test_day4():
    expected = "wednesday"
    actual = check_number(4)
    assert expected == actual


def test_day5():
    expected = "thursday"
    actual = check_number(5)
    assert expected == actual


def test_day6():
    expected = "friday"
    actual = check_number(6)
    assert expected == actual


def test_day7():
    expected = "saturday"
    actual = check_number(7)
    assert expected == actual

