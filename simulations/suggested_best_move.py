def suggest_best_move(win_probability, num_players):
    """
    Suggest the best move (fold, call, raise) based on the win probability and numbers of players.

    Args:
        win_probability (float): The player's win probability as a percentage.
        num_players (int): The total number of players in the game (including the user).

    Returns:
        str: The suggested move ('Fold', 'Call', or 'Raise')
    """
    if num_players <= 3:
        fold_threshold = 15
        raise_threshold = 40
    elif num_players <= 6:
        fold_threshold = 20
        raise_threshold = 50
    else:
        fold_threshold = 25
        raise_threshold = 60
        
    if win_probability < fold_threshold:
        return "Fold"
    elif fold_threshold <= win_probability <= raise_threshold:
        return "Call"
    else:
        return "Raise"
        