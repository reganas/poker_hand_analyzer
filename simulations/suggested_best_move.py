

def suggest_best_move(win_probability: float, num_players: int) -> str:

    if num_players <= 3:
        fold_threshold = 20
        raise_threshold = 40
    elif num_players <= 6:
        fold_threshold = 15
        raise_threshold = 30
    else:
        fold_threshold = 10
        raise_threshold = 20

    if win_probability < fold_threshold:
        return "Fold"
    elif fold_threshold <= win_probability <= raise_threshold:
        return "Call"
    else:
        return "Raise"
