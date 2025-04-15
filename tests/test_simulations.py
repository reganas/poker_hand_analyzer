from simulations.suggested_best_move import suggest_best_move


def test_best_move():
    assert suggest_best_move(win_probability=10, num_players=2) == "Fold"
    assert suggest_best_move(win_probability=20, num_players=5) == "Call"
    assert suggest_best_move(win_probability=30, num_players=8) == "Raise"
