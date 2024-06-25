old_list = [
 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(old_list: list, state: str = "EXECUTED") -> list[str]:
    """Функция которая получает список словарей и возвращает новый список,
    содержащий только те словари,у которых ключ state содержит переданное
    в функцию значение"""
    new_list = []
    new_list_for_canceled = []
    for i in old_list:
        if i.get("state") == state:
            new_list.append(i)
        else:
            new_list_for_canceled.append(i)
    return new_list


def sort_by_date(old_list: list, is_date: bool = True) -> list[str]:
    """функция которая возврашает список по убыванию"""
    sort_old_list = sorted(old_list, key=lambda x: x["date"], reverse=is_date)
    return sort_old_list


print(filter_by_state(old_list, state="EXECUTED"),)
print(sort_by_date(old_list),)
