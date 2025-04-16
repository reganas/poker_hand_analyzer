from cards.deck import Deck
from cards.cards import to_treys_format
from hands.simulate_hands import simulate_opponent_hands
from cards.validate_cards import validate_card_input
from simulations.win_probability import calculate_win_probability
from simulations.suggested_best_move import suggest_best_move
from treys import Card as TreysCard
from rich.console import Console
from main_menu_options.hand_history import HandHistory
from typing import Optional


def evaluate_hand(hand_history: HandHistory) -> None:

    console = Console()

    console.print(
        "\n[bold red]Enter 'exit' to quit or stop the program at any point of time.[/bold red]"
    )
    console.print(
        "\n[bold yellow]Valid card ranks: 2-10, valid card suits: 'spades', 'hearts', 'diamonds', or clubs.[/bold yellow]"
    )

    while True:

        deck = Deck()
        deck.shuffle()

        num_players = get_number_of_players()
        if num_players == None:
            break
        selected_cards = get_player_cards(deck)
        if selected_cards == None:
            break

        display_player_hand(console, selected_cards)

        opponent_hands = simulate_opponent_hands(
            list(selected_cards), num_opponents=num_players - 1
        )

        display_opponent_hands(console, opponent_hands)

        win_probability: float = calculate_win_probability(
            list(selected_cards), opponent_hands
        )
        console.print(
            f"\n[bold yellow]Win Probability:[/bold yellow] {win_probability:.2f}%"
        )

        best_move = suggest_best_move(win_probability, num_players)
        console.print(f"\n[bold green]Suggested Move:[/bold green] {best_move}")

        hand_history.add_hand(
            list(selected_cards), opponent_hands, win_probability, best_move
        )


def get_number_of_players() -> Optional[int]:

    while True:
        num_players_input = input(
            "\nEnter the number of players (2-10, including you): "
        )
        if num_players_input == "exit":
            print("\nExiting hand evaluation.")
            return None
        try:
            num_players = int(num_players_input)
            if 2 <= num_players <= 10:
                return num_players
            else:
                print("\nPlease enter a number between 2 and 10.")
        except ValueError:
            print(
                "\nInvalid input. Please enter a valid number of players between 2 and 10"
            )


def get_player_cards(deck: Deck) -> Optional[set]:

    selected_cards: set = set()

    while True:
        card1_input: str = input("\nEnter your first card (e.g., 'A of spades'): ")
        if card1_input == "exit":
            print("\nExiting hand evaluation")
            return None
        card1 = validate_card_input(card1_input, deck)
        if card1:
            selected_cards.add(card1)
            break

    while True:
        card2_input: str = input("\nEnter your second card (e.g., 'K of hearts'): ")
        if card2_input == "exit":
            print("\nExiting hand evaluation.")
            return None
        card2 = validate_card_input(card2_input, deck)
        if card2 and card2 not in selected_cards:
            selected_cards.add(card2)
            break
        elif card2 in selected_cards:
            print(
                "\nYou have already selected this card. Please choose a different one."
            )

    return selected_cards


def display_player_hand(console: Console, selected_cards: set) -> None:
    console.print(f"[bold blue]\nYour hand:[/bold blue]")
    treys_cards = [TreysCard.new(to_treys_format(card)) for card in selected_cards]
    TreysCard.print_pretty_cards(treys_cards)


def display_opponent_hands(console: Console, opponent_hands: list) -> None:

    for i, cards in enumerate(opponent_hands, start=1):
        console.print(f"\n[bold magenta]Opponent {i}:[/bold magenta]")
        treys_cards = [TreysCard.new(to_treys_format(card)) for card in cards]
        TreysCard.print_pretty_cards(treys_cards)
