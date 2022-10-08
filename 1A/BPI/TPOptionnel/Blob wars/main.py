import random
from itertools import product
from typing import NamedTuple


class Coordinates(NamedTuple):
    i: int
    j: int


class Move(NamedTuple):
    src: Coordinates
    dst: Coordinates


class Board:
    """
    The board used for the game
    it contains either None, or a valid player index so that
    for any coordinate (i, j)
    players_emojis[board[(i, j)]] corresponds to this player's emoji
    """

    def __init__(self, inner: list[list[int]]):
        self.inner = inner
        self.width = len(inner[0])
        self.height = len(inner)

    def __getitem__(self, *key: int) -> int:
        """
        Custom geitem so that for any coordinate (i, j),
        self.inner[i][j] == self[i, j] is True
        """
        i, j = key[0]
        return self.inner[i][j]

    def __setitem__(self, key: int, item: int | None) -> int:
        """
        Custom geitem so that for any coordinate (i, j),
        self.inner[i][j] == self[i, j] is True
        """
        i, j = key
        self.inner[i][j] = item

    def is_empty(self, coordinates: Coordinates):
        """
        Checks whether the provided coordinates do not contain anything
        """
        return self.__getitem__(coordinates) is None


class BlobWars:
    def __init__(
        self,
        board: Board | None = None,
        *,  # Blue circle, red circle
        players_emojis: list[str] = ["\U0001F535", "\U0001F534"],
        board_size: int = 8,
    ):
        if board is not None:
            self.board = board
        else:
            board_size = board_size or self.DEFAULT_BOARD_SIZE
            self.board = Board([[None] * board_size for _ in range(board_size)])

        self.players_emojis = players_emojis or self.DEFAULT_PLAYERS_EMOJIS
        self.current_player = 0
        self.number_mapping = []

    def can_move(self, piece_location: Coordinates):
        """
        Checks whether the current piece can move
        """
        p_i, p_j = piece_location

        possible_movements = [
            Coordinates(i, j)
            for i, j in product(range(p_i - 2, p_i + 3), range(p_j - 2, p_j + 3))
        ]

        return any(self.board.is_empty(coord) for coord in possible_movements)

    def can_play(self, player_index: int) -> bool:
        """
        Checks whether the current player is able to play
        by seeing if any of their piece can move
        """
        return any(
            self.can_move(Coordinates(i, j))
            for i, j in product(range(self.board.height), range(self.board.width))
            if self.board[i, j] == player_index
        )

    def fill_number_mapping(self):
        """
        fills the number mapping first
        """
        n_max = self.board.width * self.board.height
        self.number_mapping = [None] * n_max

        for i, line in enumerate(self.board.inner):
            for j, _ in enumerate(line):
                offset = i * self.board.height + self.board.width - j
                ajusted_offset = n_max - offset
                self.number_mapping[ajusted_offset] = Coordinates(i, j)

    def display_board(self):
        """
        Prints a formatted version of the board to stdout
        """
        n_max = self.board.width * self.board.height

        for i, line in enumerate(self.board.inner):
            for j, slot in enumerate(line):
                coords = Coordinates(i, j)
                if self.board.is_empty(coords):
                    offset = i * self.board.height + self.board.width - j
                    ajusted_offset = n_max - offset

                    print(f"{ajusted_offset:02}", end=" ")
                else:
                    print(self.players_emojis[self.board[i, j]], end=" ")

            print()

    def is_valid_move(
        self, current_player: int, src: Coordinates, dest: Coordinates
    ) -> bool:
        """
        Checks whether the provided move is actually valid.
        """
        # the player tried to move something that they can't
        if self.board[src.i, src.j] != current_player:
            return False

        # already occupied by their own piece
        elif not self.board.is_empty(dest) and self.board[dest] == self.board[src]:
            return False

        # too far
        elif abs(dest.i - src.i) > 2 or abs(dest.j - src.j) > 2:
            return False
        else:
            return True

    def prompt_player(self, current_player: int):
        """
        Asks the current player where he wants to play
        """
        print()
        print(
            f"Player {current_player} {self.players_emojis[self.current_player]}'s turn"
        )

        while True:
            out = input("from / to ?: ")
            try:
                from_, to = out.split()
            except ValueError:
                continue

            # Couldn't parse input
            try:
                from_ = int(from_)
                to = int(to)
            except ValueError:
                continue

            # Out of bounds, but since python allows negative indexes
            # we have to check it beforehand
            if from_ < 0 or to < 0:
                continue

            # Out of bounds
            try:
                src = self.number_mapping[from_]
                dest = self.number_mapping[to]
            except IndexError:
                continue

            # Final check
            if self.is_valid_move(self.current_player, src, dest):
                return Move(src, dest)

    def move_piece(self, move: Move):
        """
        Moves a piece from one case to another
        """
        move_max_dist = max(abs(move.src.i - move.dst.i), abs(move.src.j - move.dst.j))
        if move_max_dist == 1:
            duplication_targets = (
                (move.dst.i + 1, move.dst.j),
                (move.dst.i - 1, move.dst.j),
                (move.dst.i, move.dst.j + 1),
                (move.dst.i, move.dst.j - 1),
                move.dst
            )
            for i, j in duplication_targets:
                if i >= 0 and j >= 0:
                    try:
                        self.board[i, j] = self.board[move.src]
                    except IndexError:
                        continue
        else:
            self.board[move.dst] = self.board[move.src]
            self.board[move.src] = None

    def assign_starting_pieces(self, num_players: int):
        """
        Puts all starting pieces so that they dont overlap
        """
        available = self.number_mapping.copy()

        for n in range(num_players):
            pos = available.pop(random.randint(0, len(available) - 1))
            self.board[pos] = n

    def change_turns(self, current_player: int):
        """
        Changes turns
        """
        self.current_player = (current_player + 1) % len(self.players_emojis)

    def run(self):
        """
        Launches the game
        """
        self.fill_number_mapping()
        self.assign_starting_pieces(len(self.players_emojis))
        self.display_board()

        while self.can_play(self.current_player):
            move = self.prompt_player(self.current_player)
            self.move_piece(move)

            self.display_board()
            self.change_turns(self.current_player)

        self.change_turns(self.current_player)

        print(f"Player {self.current_player} ({self.players_emojis[self.current_player]}) won !")


def main():
    game = BlobWars()
    game.run()


if __name__ == "__main__":
    main()
