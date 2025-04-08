def evaluate_two_cards(card1, card2):
    
    rank_order = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'J': '11', 'Q': 12, 'K': 13, 'A': 14
        }
    
    rank1, rank2 = rank_order[card1.rank], rank_order[card2.rank]
    suit1, suit2 = card1.suit, card2.suit
    
    if rank1 == rank2:
        return "Pair", max(rank1, rank2)
    
    if suit1 == suit2:
        return "Suited", max(rank1, rank2)
    
    if abs(rank1 - rank2) == 1 or (rank1 ==14 and rank2 == 2):
        return "Straight Potential", max(rank1, rank2)
    
    return "High Card", max(rank1, rank2)
        
        
    
    