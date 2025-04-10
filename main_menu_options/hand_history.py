import json


class HandHistory:
    """
    A class to track, save, and load hand history.
    """
    def __init__(self, file_path):
        self.hands = []
        self.file_path = file_path

    def add_hand(self, player_hand, opponent_hands, win_probability, best_move):
       """
       Add a hand to the history:
       
       Args:
            player_hand (list): The player's hand (list of card objects).
            opponent_hands (list): The opponents' hands (list of lists of Card objects).
            probability (float): The claculated win probability.
            suggested_move (str); The suggested move for the player.
       """ 
       self.hands.append({
           "player_hand": [str(card) for card in player_hand],
           "opponent_hands": [[str(card) for card in opp_hand] for opp_hand in opponent_hands],
           "win_probability": win_probability,
           "suggested_move": best_move
       })

    def save_hands_to_file(self):
        """
        Save the hand history to a JSON file.
        """
        try:    
            with open(self.file_path, "w") as file:
                
                json.dump(self.hands, file, indent=4)
            print(f"Hand history saved to {self.file_path}.")
        
        except Exception as e:
            print(f"Error saving hand history. {e}")
                    
            
    def load_hands_from_file(self):
        """
        Load the hand history from a JSON file.
        """
        try:
            with open(self.file_path, "r") as file:
                self.hands = json.load(file)
            print(f"Hand history loaded from {self.file_path}")
        except FileNotFoundError:
            print(f"No existing hand history found. Starting fresh.")
            self.hands = []
        except json.JSONDecodeError:
            print(f"Error decoding hand history file. Starting fresh.")
            self.hands = []
        except Exception as e:
            print(f"An unexpected error occured while loading the hand history: {e}")
            self.hands = []
        
            
    def display_hands(self):
        """
        Display the history in a readable format.
        """
        if not self.hands:
            print("No hand history available.")
            return
        
        print("\nHand history")
        for i, hand in enumerate(self.hands, start=1):
            print(f"\nRound {i}:")
            print(f"  Player Hand: {', '.join(hand['player_hand'])}")
            for j, opp_hand in enumerate(hand["opponent_hands"], start=1):
                print(f"  Opponent {j} Hand: {', '.join(opp_hand)}")
            print(f"  Win Probability: {hand['win_probability']:.2f}%")
            print(f"  Suggested Move: {hand['suggested_move']}")

            
        
        
                
        