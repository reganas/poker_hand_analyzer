import pytest
from cards.cards import Card
from hands.hand_strength import evaluate_two_cards


def test_hand_strength():
    card1 = Card("5", "hearts")
    card2 = Card("5", "diamonds")
    assert evaluate_two_cards(card1, card2) == ("Pair", 5)

    card1, card2 = Card("4", "spades"), Card("K", "spades")
    assert evaluate_two_cards(card1, card2) == ("Suited", 13)

    card1, card2 = Card("8", "hearts"), Card("7", "diamonds")
    assert evaluate_two_cards(card1, card2) == ("Straight Potential", 8)

    card1, card2 = Card("A", "hearts"), Card("7", "diamonds")
    assert evaluate_two_cards(card1, card2) == ("High Card", 14)
