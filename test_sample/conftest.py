import pytest


@pytest.fixture
def fixture_value():
    return 4


@pytest.mark.parametrize("input", [10, 5, 90])
def test_check_type(input):
    #when
    subject = input

    #then
    assert isinstance(subject, int)