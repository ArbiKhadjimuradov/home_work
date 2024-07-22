import logging

logger = logging.getLogger("masks")
f_fo = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card: str) -> str:
    """Функция, которая маскирует номер карты."""
    logger.info("Проверяем точно ли введенные данные карты ровны 16 символам")
    if len(card) == 16:
        return f"{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}"
    else:
        return ""


def get_mask_account(acc_number: str) -> str:
    """Функция, которая возвращает маску счета."""
    logger.info("Проверяем точно ли введенные номера счета ровны 20 символам")
    if len(acc_number) == 25:
        return f"{'*' * 2}{acc_number[-4:]}"
    else:
        return ""


if __name__ == "__main__":
    get_mask_card_number("8990922113665229")
    get_mask_account("Счет 73654108430135874305")
