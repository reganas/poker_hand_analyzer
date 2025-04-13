class Card:
    """
    Represents a playing card with a rank and suit.
    """

    RANK_MAP = {
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "T",
        "J": "J",
        "Q": "Q",
        "K": "K",
        "A": "A",
    }

    SUIT_MAP = {"hearts": "h", "diamonds": "d", "clubs": "c", "spades": "s"}

    def __init__(self, rank: str, suit: str) -> None:
        """
        Initialize a Card object.

        Args:
            rank (str): The rank of the card (e.g. A, 2, 4, and etc.)
            suit (str): The suit of the card (e.g. 'spades', 'diamonds', and etc.)
        """
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Returns:
            str: The card in the format 'RankSuitSymbol' (e.g., 'A♠')
        """
        suit_symbols = {
            "hearts": "\u2665",
            "diamonds": "\u2666",
            "clubs": "\u2663",
            "spades": "\u2660",
        }
        return f"{self.rank}{suit_symbols[self.suit]}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the card.

        Returns:
            str: The card in the format "Card('Rank', 'Suit')"
        """

        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other: object) -> bool:
        """
        Check if two cards are equal.

        Args:
            other (object): The other card to compare.

        Returns:
            bool: True if cards are equal, False otherwise.
        """

        if isinstance(other, Card):

            return self.rank == other.rank and self.suit == other.suit
        return False

    def __hash__(self) -> int:
        """
        Return the hash value for the card.

        Returns:
            int: The hash value of the card.
        """
        return hash((self.rank, self.suit))

    @property
    def rank(self) -> str:
        """
        Get the rank of the card.

        Returns:
            str: The rank of the card.
        """
        return self._rank

    @rank.setter
    def rank(self, value: str) -> None:
        """
        Set the rank of the card.

        Args:
            value (str): The rank to set.

        Raises:
            ValueError: If the rank is invalid.
        """
        if value not in Card.RANK_MAP:
            raise ValueError(
                "Invalid rank selected. Please choose from 2-10 or A/K/Q/J"
            )
        self._rank = value

    @property
    def suit(self) -> str:
        """
        Get the suit of the card.

        Returns:
            str: The suit of the card.
        """
        return self._suit

    @suit.setter
    def suit(self, value: str) -> None:
        """
        Set the suit of the card.

        Args:
            value (str): The suit to set.

        Raises:
            ValueError: If the suit is invalid.
        """
        if value not in Card.SUIT_MAP:
            raise ValueError(
                "Invalid suit selected. Please choose from 'diamonds', spades', hearts', or 'clubs'"
            )
        self._suit = value


def to_treys_format(card: Card) -> str:
    """
    Covert a Card object to Treys format.

    Args:
        card (Card): The card to convert.

    Returns:
        str: The card in Treys format (e.g., 'Kh', '5s').
    """
    return f"{Card.RANK_MAP[card.rank]}{Card.SUIT_MAP[card.suit]}"
