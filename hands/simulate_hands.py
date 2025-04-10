import random
from cards.deck import Deck

def simulate_opponent_hands(player_cards, num_opponents):
    
    deck = Deck()
    
    deck.cards = [card for card in deck.cards if card not in player_cards] 
    
    opponent_hands = []
    for _ in range(num_opponents):
        opponent_cards = random.sample(deck.cards, 2)
        for card in opponent_cards:
            deck.cards.remove(card)
        opponent_hands.append(opponent_cards)
        
    return opponent_hands
    
