import random
from typing import List
from cards.cards import Card


class Deck:
    """
    Represents a deck of playing cards
    """

    def __init__(self) -> None:
        """
        Initialize a Deck object with 52 cards.
        """
        self._cards = [
            Card(rank, suit) for rank in Card.RANK_MAP for suit in Card.SUIT_MAP
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the deck.

        Returns:
            str: The number of cards in the deck.
        """
        return f"Deck of {self.count} cards"

    @property
    def cards(self) -> List[Card]:
        """
        Get the list of cards in the deck.

        Returns:
            List[Card]: The list of cards.
        """
        return self._cards

    @cards.setter
    def cards(self, new_cards: List[Card]) -> None:
        """
        Set the list of cards in the deck.

        Args:
            new_cards (List[Card]): The new list of cards.

        Raises:
            ValueError: If any card in the list is invalid.
        """
        for card in new_cards:
            if not isinstance(card, Card):
                raise ValueError(
                    f"Invalid card: {card}. Please choose the valid card from the deck."
                )
        self._cards = new_cards

    @property
    def count(self) -> int:
        """
        Get the number of cards in the deck.

        Returns:
            int: The number of cards.
        """
        return len(self._cards)

    def shuffle(self) -> None:
        """
        Shuffle the cards in the deck.
        """
        random.shuffle(self._cards)
