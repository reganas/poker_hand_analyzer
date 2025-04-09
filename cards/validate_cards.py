from cards.cards import Card
import re

def validate_card_input(card_input, deck):
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
            
            
        
            
        
        
        
        