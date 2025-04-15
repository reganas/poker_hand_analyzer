import json
from typing import List, Dict, Any


class HandHistory:
   
    def __init__(self, file_path: str) -> None:
        self.hands: List[Dict[str, Any]] = []
        self.file_path = file_path

    def add_hand(self, player_hand, opponent_hands, win_probability, best_move):
        
        self.hands.append(
            {
                "player_hand": [str(card) for card in player_hand],
                "opponent_hands": [
                    [str(card) for card in opp_hand] for opp_hand in opponent_hands
                ],
                "win_probability": win_probability,
                "suggested_move": best_move,
            }
        )

    def save_hands_to_file(self) -> None:
        
        try:
            with open(self.file_path, "w") as file:

                json.dump(self.hands, file, indent=4)
            print(f"Hand history saved to {self.file_path}.")

        except Exception as e:
            print(f"Error saving hand history. {e}")

    def load_hands_from_file(self) -> None:
        
        try:
            with open(self.file_path, "r") as file:
                self.hands = json.load(file)
            print(f"Hand history loaded from {self.file_path}")
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"No existing hand history found. Starting fresh.")
            self.hands = []

    def display_hands(self) -> None:
        
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
