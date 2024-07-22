from unittest.mock import patch
from src.external_api import all_amount_rub_convert
from typing import Any

transaction = ({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
})


@patch("requests.get")
def test_all_amount(mock_get: Any) -> Any:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD',
                                                         'to': 'RUB',
                                                         'amount': 8221.37},
                                               'info': {
                                                   'timestamp': 1720531985,
                                                   'rate': 87.801624},
                                               'date': '2024-07-09',
                                               'result': 721849.637505}
    assert all_amount_rub_convert(transaction) == 721849.637505


@patch('requests.get')
def test_converting_amount_transaction(mock_get, info_trans):
    mock_get.return_value.json.return_value = 31957.58
    assert all_amount_rub_convert(info_trans) == 31957.58
