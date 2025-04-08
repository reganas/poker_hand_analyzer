from collections import Counter

class Hand:
    def __init__(self, cards):
        self.cards = cards
        
    def evaluate(self):
        ranks = [card.rank for card in self.cards]
        suits = [card.suit for card in self.cards]
        
        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)
        
        rank_values = []
        rank_order = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        
        for rank in ranks:
            rank_values.append(rank_order[rank])
        rank_values = sorted(rank_values)
        
        
        is_straight = False
        if len(set(rank_values)) == 5:
            if rank_values[-1] - rank_values[0] == 4:
                is_straight = True
            elif rank_values == [2, 3, 4, 5, 14]:
                is_straight = True
                
        is_flush = 5 in suit_counts.values()
        
        if is_flush and is_straight:
            return 800 + max(rank_values) # "Straight Flush"
        
        elif 4 in rank_counts.values():
            return 700 + max(rank_values) # "Four of a Kind"
        
        elif 3 in rank_counts.values() and 2 in rank_counts.values():
            return 600 + max(rank_values) # "Full house"
        
        elif is_flush:
            return 500 + max(rank_values)
        
        elif is_straight:
            return 400 + max(rank_values) # "Straight"
            
        elif 3 in rank_counts.values():
            return 300 + max(rank_values) # "Three of a Kind"
        
        elif list(rank_counts.values()).count(2) == 2:
            return 200 + max(rank_values) # "Two pair"
        
        elif 2 in rank_counts.values():
            return 100 + max(rank_values) # "Pair"
        
        return max(rank_values) # "High Card"

        

        
    