import random
from typing import List
from hands.hand import Hand
from cards.cards import Card
from cards.deck import Deck

def evaluate_hand_strength(hand: List[Card], community_cards: List[Card]) -> int:
    full_hand = Hand(hand + community_cards)
    return full_hand.evaluate()


def simulate_round(player_hand: List[Card], opponent_hands: List[List[Card]], deck: Deck) -> bool:
    community_cards = random.sample(deck.cards, 5)
    player_strength = evaluate_hand_strength(player_hand, community_cards)
    opponent_strengths = [evaluate_hand_strength(opp_hand,community_cards) for opp_hand in opponent_hands]
    return all(player_strength >= opp_strength for opp_strength in opponent_strengths)

    

