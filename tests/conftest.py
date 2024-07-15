import pytest
from src.processing import old_list
from typing import Any


@pytest.fixture
def fixture_for_state() -> list[Any]:
    return old_list == [
        {"id": 41428829, "state": "EXECUTED", },
        {"id": 939719570, "state": "EXECUTED", },
        {"id": 594226727, "state": "CANCELED", },
        {"id": 615064591, "state": "CANCELED", },
    ]
