def get_mask_card_number(card: str) -> str:
    """Функция которая маскирует номер карты"""
    if len(card) == 16:
        return f"{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}"
    else:
        return ""


if __name__ == '__main__':
    print(get_mask_card_number("8990922113665229"))


def get_mask_account(acc_number: str) -> str:
    """Функция которая возврашает маску счета"""
    if len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4:]}"
    else:
        return ""


if __name__ == '__main__':
    print(get_mask_account("73654108430135874305"))
