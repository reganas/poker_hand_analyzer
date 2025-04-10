from cards.deck import Deck
from hands.simulate_hands import simulate_opponent_hands
from cards.validate_cards import validate_card_input
from simulations.win_probability import calculate_win_probability
from simulations.suggested_best_move import suggest_best_move

def evaluate_hand(hand_history):
    """
    Evaluate the player's hand and track the results in hand history.
    
    Args:
        hand_history (HandHistory): The HandHistory object to track the round. 
    """
    
    print ("\nEnter 'exit' to quit or stop the program at any point of time.")
    
    while True:
        
        deck = Deck()
        deck.shuffle()
    
        while True:
            num_players_input = input("\nEnter the number of players (2-10, including you): ")
            if num_players_input == "exit":
                print("\nExiting hand evaluation.")
                return
            try:
                num_players_input = int(num_players_input) 
                if 2 <= num_players_input <= 10:
                    break
                else:
                    print("\nPlease enter a number between 2 and 10.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number of players between 2 and 10")
        
        selected_cards = set()
        
        while True:
            card1_input = input("\nEnter your first card (e.g., 'A of spades'): ")
            if card1_input == "exit":
                print("\nExiting hand evaluation")
                return
            card1 = validate_card_input(card1_input, deck)
            if card1:
                selected_cards.add(card1)
                break
        
        while True:
            card2_input = input("\nEnter your second card (e.g., 'K of hearts'): ")
            if card2_input == "exit":
                print("\nExiting hand evaluation.")
                return
            card2 = validate_card_input(card2_input, deck)
            if card2 and card2 not in selected_cards:
                selected_cards.add(card2)
                break
            elif card2 in selected_cards:
                print("\nYou have already selected this card. Please choose a different one.")
        
        print(f"\nYour hand: {card1} {card2}")
        
        opponent_hands = simulate_opponent_hands([card1, card2], num_opponents=num_players_input - 1)
        for i, cards in enumerate(opponent_hands, start=1):
            print(f"\nOpponent {i}: {cards[0]} {cards[1]}\n")
        
        
        win_probability = calculate_win_probability([card1, card2], opponent_hands, deck)
        print(f"\nWin Probability: {win_probability:.2f}%")
        
        best_move = suggest_best_move(win_probability, num_players_input)
        print(f"\nSuggested Move: {best_move}")
        
        hand_history.add_hand([card1, card2], opponent_hands, win_probability, best_move)
        
        continuous_choice = input("\nType 'yes' to 'continue' or 'no' to quit the 'Hand evaluation' mode: ")
        if continuous_choice == "no":
            print("\nExiting hand evaluation.")
            break