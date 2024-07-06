import os
import json
import requests
from dotenv import load_dotenv


load_dotenv('.env')


def all_amount_transactions(transaction: [dict]) -> float:

    try:
        with open('../data/operations.json') as f:
            try:
                transaction = json.load(f)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return False
    except FileNotFoundError:
        print("Файл не найден")
        return False

    amount = float(transaction["operationAmount"]["amount"])
    currency = (transaction["operationAmount"]["currency"]["code"])
    if currency == "RUB":
        return amount
    elif currency != "RUB":
        load_dotenv()
        API_KEY = os.getenv("api_key")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text

        return result
    return False


if __name__ == '__main__':
    print(all_amount_transactions(transaction='../data/operations.json'))