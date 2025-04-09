from cards.deck import Deck
from hands.simulate_hands import simulate_opponent_hands
from cards.validate_cards import validate_card_input
from simulations.win_probability import calculate_win_probability

def main():
    deck = Deck()
    deck.shuffle()
    
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
    
    print(f"\nYour hand: {card1} {card2}")
    
    opponent_hands = simulate_opponent_hands([card1, card2], num_opponents=num_players - 1)
    for i, cards in enumerate(opponent_hands, start=1):
        print(f"\nOpponent {i}: {cards[0]} {cards[1]}\n")
    
    
    win_probability = calculate_win_probability([card1, card2], opponent_hands, deck)
    print(f"Win Probability: {win_probability:.2f}%")

if __name__ == "__main__":
    main()