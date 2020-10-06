from module_sample import square, add
import pytest


def test_square_give_correct_answer(fixture_value):
    #when
    subject = square(fixture_value)

    #then
    assert subject == 16


def test_square_not_correct_answer(fixture_value):
    #when
    subject = square(fixture_value)

    #then
    assert subject != 17


def test_add_not_correct_answer(fixture_value):
    #when
    subject = add(fixture_value, 60)

    #then
    assert subject != 10


def test_add_correct_answer(fixture_value):
    #when
    subject = add(fixture_value, 6)

    #then
    assert subject == 10


@pytest.mark.parametrize("input", [10, 5, 90])
def test_check_type(input):
    #when
    subject = input

    #then
    assert isinstance(subject, int)