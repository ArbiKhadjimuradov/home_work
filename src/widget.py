from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(cards_number:[str]) -> list[str]:
    ''' Функция которая маскирует номер карты и счета'''


    for i in cards_number:
        if i == 'Счет':
            return get_mask_account(cards_number)
        else:
            card = get_mask_card_number(cards_number[-16:])
            mask_card = cards_number.replace(cards_number[-16:],card)
            return mask_card


if __name__ == '__main__':
    print(mask_account_card('Maestro 1596837868705199'))







