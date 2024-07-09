import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv('.env')

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


def all_amount_rub_convert(transaction: dict) -> Any:
    ''' Функция возвращая сумму транзакции. '''
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return amount
        else:
            if currency or currency["operationAmount"]["currency"]["name"] != 'RUB':
                API_KEY =  'a202nweusIq4m4HXuSN60zrAxl63pz71'
                url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}'f'&amount={amount}'
                headers = {"apikey": API_KEY}
                response = requests.get(url, headers=headers)
                data = response.json()
                return data['result']
    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        return 0.0


if __name__ == '__main__':
    print(all_amount_rub_convert(transaction))
