class Card:
    RANK_MAP = {
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9', '10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'
    }
    
    SUIT_MAP = {
        'hearts': 'h', 'diamonds': 'd', 'clubs': 'c', 'spades': 's' 
    }
    
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        
    def __str__(self):
        suit_symbols = {
            'hearts': '\u2665',
            'diamonds': '\u2666',
            'clubs': '\u2663',
            'spades': '\u2660'
        }
        return f"{self.rank}{suit_symbols[self.suit]}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other):
        '''Check if two cards are equal based on rank and suit.'''
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False
    
    def __hash__(self):
        '''Allow cards to be used in sets and as dictionary keys'''
        return hash((self.rank, self.suit))
    
    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if value not in Card.RANK_MAP:
            raise ValueError("Invalid rank selected. Please choose from 2 to A")
        return self._rank
    
    @ property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value not in Card.SUIT_MAP:
            raise ValueError("Invalid suit selected. Please choose from 'diamons', spades', hearts', or 'clubs'")
        return self._suit
    
    def to_treys_format(card):
        '''
        Converts a Card object to the 'trey' format (e.g, "Ah" for Ace of hearts)
        '''
    

    
    
    
# Card symbols using Unicode
# spades = "\u2660"
# hearts = "\u2665"
# diamonds = "\u2666"
# clubs = "\u2663"

# # Display the symbols
# print("Spades:", spades)
# print("Hearts:", hearts)
# print("Diamonds:", diamonds)
# print("Clubs:", clubs)
