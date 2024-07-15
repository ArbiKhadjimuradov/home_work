import pandas as pd
import csv
import logging
from src.widget import mask_account_card
from typing import Any


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/financial.log", encoding="utf-8")
f_fo = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(f_fo)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def open_csv_data() -> Any:
    '''Функция, для чтения CSV файла.'''
    try:
        logger.info("Поиск открытие файла csv")
        with open("../data/transactions.csv", encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if 'Счет' in row['from']:
                    logger.info("В файле есть транзакции через Счет")
                    func_from = mask_account_card(row['from'])
                    func_to = mask_account_card(row['to'])
                    x = f'Транзакция', func_from, 'на', func_to
                return ' '.join(x)
    except FileNotFoundError as ex:
        logger.error(f"Ошибка {ex}")
    else:
        return []


print(open_csv_data())


def open_excel_data() -> Any:
    '''Функция, для чтения Excel файла.'''
    excel_data = pd.read_excel('../data/transactions_excel.xlsx')
    return excel_data.loc[:, ['from', 'to']]


print(open_excel_data())
