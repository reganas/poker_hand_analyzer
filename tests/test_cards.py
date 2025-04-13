import pytest
from cards.cards import Card
from cards.deck import Deck
from cards.validate_cards import validate_card_input


def test_invalid_rank():
    with pytest.raises(
        ValueError, match="Invalid rank selected. Please choose from 2-10 or A/K/Q/J"
    ):
        Card("1", "hearts")


def test_invalid_suit():
    with pytest.raises(
        ValueError,
        match="Invalid suit selected. Please choose from 'diamonds', spades', hearts', or 'clubs",
    ):
        Card("A", "ball")


def test_validate_card_input():
    deck = Deck()
    card = validate_card_input("A of spades", deck)
    assert str(card) == "A♠"
