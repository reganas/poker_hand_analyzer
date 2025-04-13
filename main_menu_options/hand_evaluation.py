from cards.deck import Deck
from cards.cards import to_treys_format
from hands.simulate_hands import simulate_opponent_hands
from cards.validate_cards import validate_card_input
from simulations.win_probability import calculate_win_probability
from simulations.suggested_best_move import suggest_best_move
from treys import Card as TreysCard
from rich.console import Console
from main_menu_options.hand_history import HandHistory


def evaluate_hand(hand_history: HandHistory) -> None:
    """
    Evaluate the player's hand and track the results in hand history.

    Args:
        hand_history (HandHistory): The HandHistory object to track the round.

    """

    print("\nEnter 'exit' to quit or stop the program at any point of time.")
    print(
        "\nValid card ranks: 2-10, valid card suits: 'spades', 'hearts', 'diamonds', or clubs."
    )

    while True:

        deck = Deck()
        deck.shuffle()
        console = Console()

        while True:
            num_players_input = input(
                "\nEnter the number of players (2-10, including you): "
            )
            if num_players_input == "exit":
                print("\nExiting hand evaluation.")
                return
            try:
                num_players = int(num_players_input)
                if 2 <= num_players <= 10:
                    break
                else:
                    print("\nPlease enter a number between 2 and 10.")
            except ValueError:
                print(
                    "\nInvalid input. Please enter a valid number of players between 2 and 10"
                )

        selected_cards: set = set()

        while True:
            card1_input: str = input("\nEnter your first card (e.g., 'A of spades'): ")
            if card1_input == "exit":
                print("\nExiting hand evaluation")
                return
            card1 = validate_card_input(card1_input, deck)
            if card1:
                selected_cards.add(card1)
                break

        while True:
            card2_input: str = input("\nEnter your second card (e.g., 'K of hearts'): ")
            if card2_input == "exit":
                print("\nExiting hand evaluation.")
                return
            card2 = validate_card_input(card2_input, deck)
            if card2 and card2 not in selected_cards:
                selected_cards.add(card2)
                break
            elif card2 in selected_cards:
                print(
                    "\nYou have already selected this card. Please choose a different one."
                )

        console.print(f"[bold blue]\nYour hand:[/bold blue]")
        treys_cards = [TreysCard.new(to_treys_format(card)) for card in [card1, card2]]
        TreysCard.print_pretty_cards(treys_cards)

        opponent_hands = simulate_opponent_hands(
            [card1, card2], num_opponents=num_players - 1
        )
        for i, cards in enumerate(opponent_hands, start=1):
            console.print(f"\n[bold magenta]Opponent {i}:[/bold magenta]")
            treys_cards = [TreysCard.new(to_treys_format(card)) for card in cards]
            TreysCard.print_pretty_cards(treys_cards)

        win_probability: float = calculate_win_probability(
            [card1, card2], opponent_hands
        )
        console.print(
            f"\n[bold yellow]Win Probability:[/bold yellow] {win_probability:.2f}%"
        )

        best_move = suggest_best_move(win_probability, num_players)
        console.print(f"\n[bold green]Suggested Move:[/bold green] {best_move}")

        hand_history.add_hand(
            [card1, card2], opponent_hands, win_probability, best_move
        )

        continuous_choice: str = input(
            "\nType 'yes' to 'continue' or 'no' to quit the 'Hand evaluation' mode: "
        )
        if continuous_choice == "no":
            print("\nExiting hand evaluation.")
            break
