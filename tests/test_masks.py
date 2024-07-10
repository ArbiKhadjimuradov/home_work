from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"

    assert len(get_mask_account("**4305")) == 0


def test_get_mask_account_for_emty():
    assert get_mask_account("") == ""


def test_get_mask_card_number():
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"


def test_get_mask_card_number_for_emty():
    assert get_mask_card_number("") == ""
