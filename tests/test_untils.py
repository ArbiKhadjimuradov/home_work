from src.utils import get_operations_info
from typing import Any


def get_info_json_object(capsys: Any) -> Any:
    get_operations_info(filename='../data/abdula.json')
    captured = capsys.readouterr()
    assert captured.out == 'FileNotFoundError'


def test_info_json_emty(capsys: Any) -> Any:
    get_operations_info(filename='')
    captured = capsys.readouterr()
    assert captured.out == ''
