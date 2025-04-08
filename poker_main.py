# Output:
# Welcome to the Poker Hand Analyzer & Strategy Guide!

# Main menu:
# 1. Input your hand
# 2. Simulate a round
# 3. View hand history
# 4. Exit

# Choose an option: 1

# Enter your hand (e.g., "A♠ K♦ 10♣ 5♥ 2♠"): A♠ K♦ 10♣ 5♥ 2♠
# Evaluating hand...
# Your hand: High Card (Ace)
# Win Probability: 12.7%
# Suggested Move: Fold
from deck import Deck
from cards import Card
from hand_strength import evaluate_two_cards
from simulate_hands import simulate_opponent_hands
from validate_cards import validate_card_input
from win_probability import calculate_win_probability
import re

def main():
    deck = Deck()
    deck.shuffle()
    
    # Card1 = input("Enter your first card (e.g. '2 of spades'): ")
    # Card2 = input("Enter your second card (e.g. '3 of diamonds'): ")
    
    while True:
        try:
            num_players = int(input("Enter the number of players (2-10, including you): "))
            if 2 <= num_players <= 10:
                break
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number of players between 2 and 10")
    
    selected_cards = set()
    
    while True:
        card1_input = input("Enter your first card (e.g., 'A of spades'): ")
        card1 = validate_card_input(card1_input, deck)
        if card1:
            selected_cards.add(card1)
            break
    
    while True:
        card2_input = input("Enter your second card (e.g., 'K of hearts'): ")
        card2 = validate_card_input(card2_input, deck)
        if card2 and card2 not in selected_cards:
            selected_cards.add(card2)
            break
        elif card2 in selected_cards:
            print("You have already selected this card. Please choose a different one.")
    
    # rank1, _, suit1 = card1_input.partition(" of ")
    # rank2, _, suit2 = card2_input.partition(" of ")
    
    # card1 = Card(rank1.strip().capitalize(), suit1.strip())
    # card2 = Card(rank2.strip().capitalize(), suit2.strip())
    
    print(f"\nYour hand: {card1} {card2}")
    
    opponent_hands = simulate_opponent_hands([card1, card2], num_opponents=num_players - 1)
    for i, cards in enumerate(opponent_hands, start=1):
        print(f"\nOpponent {i}: {cards[0]} {cards[1]}\n")
    
    
    win_probability = calculate_win_probability([card1, card2], opponent_hands, deck)
    print(f"Win Probability: {win_probability:.2f}%")
        
        
         
    


if __name__ == "__main__":
    main()