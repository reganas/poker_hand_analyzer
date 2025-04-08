import random
from deck import Deck
from hand_strength import evaluate_two_cards

def simulate_opponent_hands(player_cards, num_opponents):
    '''Simulate opponent hands and compare their strength with the player's hand.'''
    deck = Deck()
    # to make sure opponents hands are different from player's hand
    deck.cards = [card for card in deck.cards if card not in player_cards] # Remove player's cards
    
    # opponent_strengths = []
    # for _ in range(num_opponents):
    #     opponent_cards = random.sample(deck.cards, 2)
    #     strength, high_card = evaluate_two_cards(opponent_cards[0], opponent_cards[1])
    #     opponent_strengths.append((opponent_cards, strength, high_card))
        
    # return opponent_strengths
        
    opponent_hands = []
    for _ in range(num_opponents):
        opponent_cards = random.sample(deck.cards, 2)
        for card in opponent_cards:
            deck.cards.remove(card)
        opponent_hands.append(opponent_cards)
        
    return opponent_hands
    