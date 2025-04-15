from cards.cards import to_treys_format
from treys import Evaluator, Deck as TreysDeck, Card as TreysCard
from cards.cards import Card
from typing import List


def calculate_win_probability(player_hand: List[Card], opponent_hands: List[List[Card]], num_simulations: int = 10000) -> float:
    
    evaluator = Evaluator()
    wins = 0

    player_hand_treys = []
    for card in player_hand:
        treys_card = TreysCard.new(to_treys_format(card))
        player_hand_treys.append(treys_card)

    opponent_hands_treys = []
    for opp_hand in opponent_hands:
        treys_opp_hand = []
        for card in opp_hand:
            treys_card = TreysCard.new(to_treys_format(card))
            treys_opp_hand.append(treys_card)
        opponent_hands_treys.append(treys_opp_hand)

    for _ in range(num_simulations):

        treys_deck = TreysDeck()

        all_cards_in_play = player_hand_treys + sum(opponent_hands_treys, [])

        for card in all_cards_in_play:
            treys_deck.cards.remove(card)

        community_cards = treys_deck.draw(5)

        player_score = evaluator.evaluate(player_hand_treys, community_cards)

        opponent_scores = [
            evaluator.evaluate(opp_hand, community_cards)
            for opp_hand in opponent_hands_treys
        ]

        if all(player_score <= opp_score for opp_score in opponent_scores):
            wins += 1

    win_probability = (wins / num_simulations) * 100
    return win_probability
