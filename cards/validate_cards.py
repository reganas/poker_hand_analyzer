from cards.cards import Card
import re
from cards.deck import Deck
from typing import Optional


def validate_card_input(card_input: str, deck: Deck) -> Optional[Card]:
    
    pattern = r"([2-9]|10|[JQKA])\s+of\s+(hearts|diamonds|clubs|spades)"
    match = re.match(pattern, card_input.strip(), re.IGNORECASE)
    if not match:
        print("Invalid input format. Please enter a valid card (e.g., 'A of spades').")
        return None
        
    rank, suit = match.group(1).upper(), match.group(2).lower()
    card = Card(rank, suit)
    if card not in deck.cards:  
        print("Card not in the deck. Please choose a valid card.")
        return None

    print(f"User input card: {card}")
    return card
        
