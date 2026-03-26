from app.main import get_human_age


def test_should_return_zero_when_zero_passed() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_one_when_first_period_passed() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_first_period_end_returns_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_period_start_returns_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_second_period_end_returns_two() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_third_period_start_should_return_diff_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_one_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
