from src.generators import (card_number_generator,
                            transactions,
                            transaction_descriptions,
                            filter_by_currency)


def test_filter_by_currency():
    generator = filter_by_currency(transactions, cur="USD")
    assert next(generator)["id"] == 939719570
    assert next(generator)["id"] == 142264268


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(start=1, end=5)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    assert next(generator) == '0000 0000 0000 0003'
    assert next(generator) == '0000 0000 0000 0004'
    assert next(generator) == '0000 0000 0000 0005'
