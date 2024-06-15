from datetime import datetime
from masks import get_mask_account, get_mask_card_number
from typing import Any


def mask_account_card(cards_number: str) -> str:
    """Функция которая маскирует номер карты и счета."""

    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[:])}"
        return mask_account
    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


def get_data(data: Any) -> Any:
    """Функция которая возврашает дату"""

    d = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(get_data("2018-07-11T02:26:18.671407"))
