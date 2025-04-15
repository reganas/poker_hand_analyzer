import random
from typing import List
from cards.cards import Card


class Deck:
    
    def __init__(self) -> None:
        
        self._cards = [
            Card(rank, suit) for rank in Card.RANK_MAP for suit in Card.SUIT_MAP
        ]

    def __str__(self) -> str:
        
        return f"Deck of {self.count} cards"

    @property
    def cards(self) -> List[Card]:
        
        return self._cards

    @cards.setter
    def cards(self, new_cards: List[Card]) -> None:
        
        for card in new_cards:
            if not isinstance(card, Card):
                raise ValueError(
                    f"Invalid card: {card}. Please choose the valid card from the deck."
                )
        self._cards = new_cards

    @property
    def count(self) -> int:
        
        return len(self._cards)

    def shuffle(self) -> None:
        
        random.shuffle(self._cards)
