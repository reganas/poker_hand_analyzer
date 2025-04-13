# Poker Hand Analyzer

### Poker Game Rules

Poker is a popular card game that combines skill, strategy, and luck. The goal is to form the best possible hand or convince opponents to fold. Below are the basic rules:

1. **Hand Rankings** (from highest to lowest):
   - **Royal Flush**: A, K, Q, J, 10 of the same suit.
   - **Straight Flush**: Five consecutive cards of the same suit.
   - **Four of a Kind**: Four cards of the same rank.
   - **Full House**: Three cards of one rank and two of another.
   - **Flush**: Five cards of the same suit.
   - **Straight**: Five consecutive cards of any suit.
   - **Three of a Kind**: Three cards of the same rank.
   - **Two Pair**: Two pairs of cards with the same rank.
   - **One Pair**: Two cards of the same rank.
   - **High Card**: The highest card when no other hand is formed.

2. **Gameplay**:
   - Each player is dealt two private cards (hole cards).
   - Five community cards are dealt face-up on the table in three stages:
     - **The Flop**: First three community cards.
     - **The Turn**: Fourth community card.
     - **The River**: Fifth and final community card.
   - Players use their two hole cards and the five community cards to form the best five-card hand.

3. **Betting Rounds**:
   - **Pre-Flop**: After players receive their hole cards.
   - **Post-Flop**: After the flop is dealt.
   - **Post-Turn**: After the turn is dealt.
   - **Post-River**: After the river is dealt.
   - Players can choose to **fold**, **call**, **raise**, or **check** during each betting round.

4. **Winning**:
   - The player with the best hand at the showdown wins the pot.
   - Alternatively, a player can win if all opponents fold.

# Overview
This project simulates a poker hand evaluator that evaluates the player's and opponents' hands, win probabilities, and suggests moves as per user's input.

# Features
- Hand Evaluation
- Opponent Hand simulation
- Win Probability Estimation
- Suggested moves
- Hand history
- Interactive CLI for user input


# How to start:

## 1. Clone the repository:

- git clone https://github.com/your-repo/poker-hand-analyzer.git
- cd poker-hand-analyzer

## 2. Install necessary packages using:

- pip install -r requirements.txt

## 3. To run unit tests use the following command-line:

- pytest tests

4. ## To check type hints run in the terminal:

- mypy . --ignore-missing-imports

5. ## To run the program, use the following command-line:

- python main.py

6. ## Requirements

- Python 3.8 or higher
- pip (Python package manager)






