import pytest

from main import is_even, is_odd, add, fetch_weather


@pytest.fixture
def even_numbers():
    return [2, 4, 22, 10, 12, 22]  # sformuvali znachenya tut


@pytest.fixture  # is as dependencies, zavisimosti, fixtura srabativaet pered zapuskom nswey programmi
def odd_numbers():
    return [1, 3, 5, 13, 11, 15, 23]  # i tut


def test_is_even(even_numbers, odd_numbers):  # tut budetnaxoditsya result vvishshe funccii
    for i in even_numbers:
        assert is_even(4) is True

    for j in odd_numbers:
        assert is_even(5) is False


def test_is_odd(even_numbers, odd_numbers):
    for i in even_numbers:
        assert is_odd(5) is True

    for j in odd_numbers:
        assert is_odd(6) is False


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (3, 3, 6), (0, 1, 1), (-1, -2, -3)])
def test_add(a, b, expected):  # tut vse rospakuetsya
    assert add(a, b) == expected


def test_fetch_weather(mocker):
    api_call_mocked = mocker.patch("main.api_request", return_value="Cloudy")

    result = fetch_weather("London")

    api_call_mocked.assert_called()  # vivodit bulali vizvana eta func

    assert result == "Weather in London: Cloudy"
