from cards.cards import Card
import re
from cards.deck import Deck
from typing import Optional


def validate_card_input(card_input: str, deck: Deck) -> Optional[Card]:
    """
    Validate user's card input and check if it's in the deck.

    Args:
        card_input (str): The user's input (e.g. 'K of spades')
        deck (Deck): The deck to check the card against.

    Returns:
        Optional[Card]: Validated card object, or None if card is invalid.
    """
    pattern = r"([2-9]|10|[JQKA])\s+of\s+(hearts|diamonds|clubs|spades)"
    match = re.match(pattern, card_input.strip(), re.IGNORECASE)
    if match:
        rank, suit = match.group(1).upper(), match.group(2).lower()
        card = Card(rank, suit)
        print(f"User input card: {card}")
        if card in deck.cards:
            return card
        else:
            print("Card not in the deck. Please choose a valid card.")
            return None
    else:
        print("Invalid input format. Please enter a valid card (e.g., 'A of spades').")
        return None
