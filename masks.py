def get_mask_card_number(card: str) -> str:
    """Функция которая маскирует номер карты"""
    return f"{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}"

if __name__ == '__main__':
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(acc_number: str) -> str:
    """Функция которая возврашает маску счета"""
    return f"{'*' * 2}{acc_number[-4:]}"

if __name__ == '__main__':
    print(get_mask_account("73654108430135874305"))
