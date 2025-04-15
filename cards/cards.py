class Card:
    
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
        
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        
        suit_symbols = {
            "hearts": "\u2665",
            "diamonds": "\u2666",
            "clubs": "\u2663",
            "spades": "\u2660",
        }
        return f"{self.rank}{suit_symbols[self.suit]}"

    def __repr__(self) -> str:
        
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other: object) -> bool:

        if isinstance(other, Card):

            return self.rank == other.rank and self.suit == other.suit
        return False

    def __hash__(self) -> int:
        
        return hash((self.rank, self.suit))

    @property
    def rank(self) -> str:
        
        return self._rank

    @rank.setter
    def rank(self, value: str) -> None:
        
        if value not in Card.RANK_MAP:
            raise ValueError(
                "Invalid rank selected. Please choose from 2-10 or A/K/Q/J"
            )
        self._rank = value

    @property
    def suit(self) -> str:
        
        return self._suit

    @suit.setter
    def suit(self, value: str) -> None:
        
        if value not in Card.SUIT_MAP:
            raise ValueError(
                "Invalid suit selected. Please choose from 'diamonds', spades', hearts', or 'clubs'"
            )
        self._suit = value


def to_treys_format(card: Card) -> str:
    
    return f"{Card.RANK_MAP[card.rank]}{Card.SUIT_MAP[card.suit]}"
