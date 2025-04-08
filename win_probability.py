import random
# from hand import Hand
from treys import Card, Evaluator, Deck

def calculate_win_probability(player_hand, opponent_hands, deck, num_simulations=10000):
    """
    Calculate the win probability for the player's hand.
    
    Args:
        player_hand (list): The player's two cards.
        opponent_hands (list): A list of opponents' hands (each hand is a list of two cards).
        deck (Deck): The deck of cards
        num_simulations (int): Number of simulations to run.
        
    Returns:
        float: The win probability as a percentage.
    """
    evaluator = Evaluator()
    wins = 0
    
    # Convert player's hand and opponent hands to 'treys' format
    player_hand_treys = []
    for card in player_hand:
        treys_card = Card.new(str(card))
        player_hand_treys.append(treys_card)
        
    opponent_hands_treys = []
    for opp_hand in opponent_hands:
        treys_opp_hand = []
        for card in opp_hand:
            treys_card = Card.new(str(card))
            treys_opp_hand.append(treys_card)
        opponent_hands_treys.append(treys_opp_hand)
    
    for _ in range(num_simulations):
        
        # Generate a new deck and remove cards already in play
        treys_deck = Deck()
        
        # Combine player's cards and opponent's cards into a single list
        all_cards_in_play = player_hand_treys + sum(opponent_hands_treys, [])
        
        for card in all_cards_in_play:
            treys_deck.cards.remove()
        
        # Deal 5 community cards    
        community_cards = treys_deck.draw(5)
        
        # Evaluate player's hand
        player_score = evaluator.evaluate(player_hand_treys, community_cards)
        
        # Evaluate opponents' hand
        opponent_scores = [
            evaluator.evaluate(opp_hand, community_cards) for opp_hand in opponent_hands_treys
        ]
        
        # Check if the player's hand is the best
        if all(player_score <= opp_score for opp_score in opponent_scores): # lower score is better
            wins += 1
        
    win_probability = (wins / num_simulations) * 100
    return win_probability
        # Generate 5 random community cards
    #     remaining_deck = [card for card in deck.cards if card not in player_hand and all(card not in opp for opp in opponent_hands)]
    #     community_cards = random.sample(remaining_deck, 5)
        
    #     # Evaluate player's full hand
    #     player_full_hand = Hand(player_hand + community_cards)
    #     player_strength = player_full_hand.evaluate()
        
    #     # Evaluate opponents' full hands
    #     opponent_strengths = []
    #     for opponent_hand in opponent_hands:
    #         opponent_full_hand = Hand(opponent_hand + community_cards)
    #         opponent_strengths.append(opponent_full_hand.evaluate())
            
    #     if all(player_strength >= opponent_strength for opponent_strength in opponent_strengths):
    #         wins += 1
            
    # win_probability = (wins / num_simulations) * 100
    # return win_probability
        