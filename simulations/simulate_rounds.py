import random
from typing import List
from hands.hand import Hand
from cards.cards import Card
from cards.deck import Deck


def simulate_round(player_hand: List[Card], opponent_hands: List[List[Card]], deck: Deck) -> bool:
    """
    Simulate a single round of the game.

    Args:
        player_hand (List[Card]): The player's hand (list of two Card objects).
        opponent_hands (List[List[Card]]): A list of hands for each opponent (each hand is a list of two Card objects).
        deck (Deck): The deck of cards to draw community cards from.

    Returns:
        bool: True if the player wins the round, False otherwise.
    """

    community_cards: List[Card] = random.sample(deck.cards, 5)

    player_full_hand = Hand(player_hand + community_cards)
    player_strength = player_full_hand.evaluate()

    opponent_strengths: List[int] = []
    for opponent_hand in opponent_hands:
        opponent_full_hand = Hand(opponent_hand + community_cards)
        opponent_strengths.append(opponent_full_hand.evaluate())

    if all(
        player_strength >= opponent_strength for opponent_strength in opponent_strengths
    ):
        return True
    return False
