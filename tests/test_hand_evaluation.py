import pytest
from main_menu_options.hand_evaluation import get_number_of_players


def test_get_number_of_players(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert get_number_of_players() == 2

    monkeypatch.setattr("builtins.input", lambda _: "exit")
    assert get_number_of_players() is None
