from collections import Counter
from typing import List


class Hand:
    def __init__(self, cards: List) -> None:
        self.cards = cards

    @staticmethod
    def rank_to_value(rank: str) -> int:
        
        rank_order = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        return rank_order[rank]

    def evaluate(self) -> int:
        
        ranks = [card.rank for card in self.cards]
        suits = [card.suit for card in self.cards]

        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)

        rank_values = sorted([Hand.rank_to_value(rank) for rank in ranks])

        is_straight = False
        if len(set(rank_values)) == 5:
            if rank_values[-1] - rank_values[0] == 4:
                is_straight = True
            elif rank_values == [2, 3, 4, 5, 14]:
                is_straight = True

        is_flush = 5 in suit_counts.values()

        if is_flush and is_straight:
            return 800 + max(rank_values)

        elif 4 in rank_counts.values():
            return 700 + max(rank_values)

        elif 3 in rank_counts.values() and 2 in rank_counts.values():
            return 600 + max(rank_values)

        elif is_flush:
            return 500 + max(rank_values)

        elif is_straight:
            return 400 + max(rank_values)

        elif 3 in rank_counts.values():
            return 300 + max(rank_values)

        elif list(rank_counts.values()).count(2) == 2:
            return 200 + max(rank_values)

        elif 2 in rank_counts.values():
            return 100 + max(rank_values)

        return max(rank_values)
