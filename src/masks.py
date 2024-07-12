import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card: str) -> str:
    """ Функция, которая маскирует номер карты"""

    logger.info(f'Проверяем точно ли введенные данные карты ровны 16 символам')
    if len(card) == 16:
        return f"{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}"
    else:
        logger.error(f'Введенные данные не корректны')
        return ""


if __name__ == '__main__':
    print(get_mask_card_number("8990922113665229"))


def get_mask_account(acc_number: str) -> str:
    """Функция, которая возврашает маску счета"""

    logger.info(f'Проверяем точно ли введенные номера счета ровны 20 символам')
    if len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4:]}"
    else:
        logger.error(f'Введенные данные не корректны')
        return ""


if __name__ == '__main__':
    print(get_mask_account("73654108430135874305"))
