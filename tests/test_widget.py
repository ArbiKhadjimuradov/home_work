import pytest
from src.widget import mask_account_card, get_data
from typing import Any


def test_mask_account() -> Any:
    assert (mask_account_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229")


def test_mask_account_for_emty() -> Any:
    assert mask_account_card("") == ""


def test_get_data() -> Any:
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_get_data_for_emty() -> Any:
    assert get_data("") == ""


@pytest.mark.parametrize("data, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2019-07-03T18:35:29.512364", "03.07.2019")
])
def test_get_data_add(data: str, expected: str) -> Any:
    assert get_data(data) == expected
