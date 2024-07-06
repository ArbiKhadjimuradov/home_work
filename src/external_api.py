import os
import json
import requests
from dotenv import load_dotenv


load_dotenv('.env')

transaction = ({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  })


def all_amount_rub_convert(transaction: dict) -> float:
    ''' Функция возвращая сумму транзакции. '''
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return amount
        else:
            API_KEY = os.getenv("api_key")
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            data = response.json()
            return data["result"]
    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        return 0.0

        # # elif ['currency'] != "RUB":
        # #     load_dotenv()
        # #     API_KEY = os.getenv("API_KEY")
        # #
        # #     response = requests.get("https://api.apilayer.com/exchangerates_data/convert", headers={"apikey": API_KEY}, params={'from': currency, 'to': 'RUB', 'amount': amount})
        # #     status_code = response.status_code
        # #     result = response.text
        # #     if response.status_code == 200:
        # #         transaction = response.json()
        # #     elif 'result' in transaction:
        # #         amount = transaction['result']
        # #     else:
        # #         raise ValueError(f'Exchange rate for {currency} not found in API response')
        #     return index


if __name__ == '__main__':
    print(all_amount_rub_convert(transaction))