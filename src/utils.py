import os
import json


def get_operations_info(filename: str) -> list[dict]:
    try:
        with open(filename, 'r', encoding='utf8') as f:
            data_info = json.load(f)
            if type(data_info) is not list:
                return []
    except FileNotFoundError:
        return []
    else:
        return data_info


if __name__ == '__main__':
    print(get_operations_info(filename='../data/operations.json'))
