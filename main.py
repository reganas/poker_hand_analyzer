from main_menu_options.hand_evaluation import evaluate_hand
from main_menu_options.hand_history import HandHistory
from utilities.utils import display_main_menu


def main():
    hand_history = HandHistory("hand_history.json")
    hand_history.load_hands_from_file()

    while True:
        choice = display_main_menu()

        if choice == "1":
            evaluate_hand(hand_history)
        elif choice == "2":
            hand_history.display_hands()
        elif choice == "3":
            hand_history.save_hands_to_file()
            print("Exiting the program. Hand history saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
