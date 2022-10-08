#! /usr/bin/python3
import sys
import random

from typing import NamedTuple, NewType
from string import ascii_uppercase

Board = NewType("Board", list[list[bool]])

MAX_WIDTH = 9
MAX_HEIGHT = 9


class BoardSize(NamedTuple):
    width: int
    height: int


class Coordinates(NamedTuple):
    i: int
    j: int


class LightsOut:
    def __init__(self, board: Board | None):
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.forfeited = False

        self.turns_played = 0

    @classmethod
    def from_board(cls, board: Board):
        return cls(board)

    @classmethod
    def from_board_size(cls, board_size: BoardSize):
        """
        Creates a new random board using provided sizes
        """
        board = [[False] * board_size.width for _ in range(board_size.height)]

        for i in range(board_size.height):
            for j in range(board_size.width):
                board[i][j] = random.choice([True, False])

        return cls(board)

    @classmethod
    def from_filename(cls, filename: str, **kwargs):
        """
        Opens the file and creates a new session using the provided board
        """
        board = []

        with open(filename, "r", **kwargs) as file:
            for line in file:
                board.append([char == "." for char in line[:-1]])

        return cls.from_board(board)

    def has_any_lights_on(self) -> bool:
        """
        Checks whether the board has any lights on
        """
        return any(any(x for x in line) for line in self.board)

    def should_keep_running(self):
        return self.has_any_lights_on() and not self.forfeited

    def parse_user_input(self, x_input: str, y_input: str) -> Coordinates | None:
        """
        Turns an user input such as A3 into proper coordinates
        Returns None if unable to
        """
        try:
            i = ascii_uppercase.index(x_input.upper())
        except IndexError:  # Not a letter
            return None

        try:
            j = int(y_input) - 1
        except ValueError:  # Not an int
            return None

        try:
            self.board[i][j]
        except IndexError:  # Out of bounds
            return None

        return Coordinates(i, j)

    def flip_tiles(self, at: Coordinates):
        """
        Flip tiles according to Lights Out's rules
        """
        i, j = at
        to_flip = [
            (i, j),  # Same
            (i + 1, j),  # Right
            (i - 1, j),  # Left
            (i, j - 1),  # Above
            (i, j + 1),  # Below
        ]

        for x, y in to_flip:
            if x < 0 or y < 0:
                continue
            try:
                self.board[x][y] = not self.board[x][y]
            except IndexError:
                continue

    def get_user_input(self) -> None | Coordinates:
        """
        Prompts the user for an input until they provide proper coordinates
        """
        while True:
            try:
                x, y = input("Enter a tile that should be switched (ex: A5): ")
            except KeyboardInterrupt:
                return None

            parsed = self.parse_user_input(x, y)

            if parsed is not None:
                return parsed

    @staticmethod
    def format_line(line: list[bool]) -> str:
        """
        Formats a line so that it gets it's own separator
        """
        out = []

        for char in line:
            if char:
                out.append(" O ")
            else:
                out.append("   ")

        return " | ".join(out)

    def display_board(self):
        """
        Displays the board on stdout
        """
        print(" " * 5, end="")
        for i in range(1, self.width + 1):
            print(i, end=" " * 5)
        print()

        horizontal_sep = "  " + ("+" + "-" * 5) * self.width + "+"
        vertical_seps = "  | " + self.format_line([False] * (self.width + 1))

        print(horizontal_sep)
        for letter, line in zip(ascii_uppercase, self.board):
            print(vertical_seps)
            print(letter, "| " + self.format_line(line) + " |")
            print(vertical_seps)
            print(horizontal_sep)

    def game_won(self):
        """
        Ran when the board has been cleared
        """
        print(f"GG ! You solved the puzzle in {self.turns_played} moves")

    def game_lost(self):
        """
        Ran when the player gave up
        """
        print(f"\nYou attempted {self.turns_played} before giving up.")

    def run(self):
        self.display_board()

        while self.should_keep_running():
            self.turns_played += 1
            chosen_coordinates = self.get_user_input()

            if chosen_coordinates is None:
                self.forfeited = True
            else:
                self.flip_tiles(chosen_coordinates)
                self.display_board()

        if self.forfeited:
            self.game_lost()
        else:
            self.game_won()


def create_game(args: list[str]) -> list[LightsOut]:
    if not args:
        board_size = BoardSize(
            random.randint(2, MAX_WIDTH), random.randint(2, MAX_HEIGHT)
        )
        return [LightsOut.from_board_size(board_size)]
    elif len(args) == 1:
        return [LightsOut.from_filename(args[0])]

    elif len(args) >= 2:
        return [LightsOut.from_filename(arg) for arg in args]


def main():
    games = create_game(sys.argv[1:])
    for game in games:
        game.run()


if __name__ == "__main__":
    main()
