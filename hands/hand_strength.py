from hands.hand import Hand
from cards.cards import Card
from typing import Tuple


def evaluate_two_cards(card1: Card, card2: Card) -> Tuple[str, int]:

    rank1, rank2 = Hand.rank_to_value(card1.rank), Hand.rank_to_value(card2.rank)
    suit1, suit2 = card1.suit, card2.suit

    if rank1 == rank2:
        return "Pair", max(rank1, rank2)

    if suit1 == suit2:
        return "Suited", max(rank1, rank2)

    if abs(rank1 - rank2) == 1 or (rank1 == 14 and rank2 == 2):
        return "Straight Potential", max(rank1, rank2)

    return "High Card", max(rank1, rank2)
