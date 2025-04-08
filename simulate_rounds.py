import random
from hand import Hand

def simulate_round(player_hand, opponent_hands, deck):
    
    community_cards = random.sample(deck.cards, 5)
    
    player_full_hand = Hand(player_hand + community_cards)
    player_strength = player_full_hand.evaluate()
    
    opponent_strengths = []
    for opponent_hand in opponent_hands:
        opponent_full_hand = Hand(opponent_hand + community_cards)
        opponent_strengths.append(opponent_full_hand.evaluate())
        
    if all(player_strength >= opponent_strength for opponent_strength in opponent_strengths):
        return True
    return False
    