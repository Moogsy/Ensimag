#! /usr/bin/env python3
"""Papier caillou ciseaux"""

import random

PLAYS = ("rock", "paper", "scissors")


def compare_choices(player_choice: str, computer_choice: str) -> str:
    """
    Returns a string announcing this game's outcome
    """
    if player_choice == computer_choice:
        return "draw"
    elif PLAYS[(PLAYS.index(player_choice) + 1) % 3] == computer_choice:
        return "defeat"
    else:
        return "victory"


def main():
    """Lance ne partie de pierre papier ciseau"""

    while True:
        try:
            player_choice = input("rock / paper / scissors / exit ? ")
        except Exception:  # type: ignore
            break

        computer_choice = random.choice(PLAYS)

        if player_choice == "exit":
            break

        if player_choice in PLAYS:
            outcome = compare_choices(player_choice, computer_choice)
        else:
            print("Invalid choice")
            continue

        print(f"{outcome} ! computer chose: {computer_choice}")

    print("Goodbye")


if __name__ == "__main__":
    main()
