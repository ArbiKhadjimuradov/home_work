import unittest
from unittest.mock import patch
import pandas as pd
from src.financial import open_csv_data, open_excel_data
from typing import Any

transaction = ({
    'id': 650703,
    'state': 'EXECUTED',
    'date': '2023-09-05T11:30:32Z',
    'amount': '16210',
    'currency_name': 'Sol',
    'currency_code': 'PEN',
    'from': 'Счет 58803664561298323391',
    'to': 'Счет 39745660563456619397',
    'description': 'Перевод организации'})


@patch("requests.get")
def get_info_csv_object(mock_get: Any) -> Any:
    mock_get.return_value.csv.return_value = transaction
    assert open_csv_data() == transaction.get('from'), transaction.get('to')
