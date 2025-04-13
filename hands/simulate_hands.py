import random
from typing import List
from cards.deck import Deck


def simulate_opponent_hands(player_cards: List, num_opponents: int) -> List[List]:
    """
    Simulate opponent hands by randomly selecting cards from the deck.

    Args:
        player_cards (List): The player's cards to exclude fro mthe deck.
        num_opponents (int): The number of opponents

    Returns:
        List[List]: A list of hands for each opponent.
    """
    deck = Deck()

    deck.cards = [card for card in deck.cards if card not in player_cards]

    opponent_hands: List[List] = []
    for _ in range(num_opponents):
        opponent_cards = random.sample(deck.cards, 2)
        for card in opponent_cards:
            deck.cards.remove(card)
        opponent_hands.append(opponent_cards)

    return opponent_hands
