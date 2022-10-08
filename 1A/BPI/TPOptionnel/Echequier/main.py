import sys
import svg


def divisors(n: int) -> list[int]:
    """
    Returns a lilst of n's divisors
    """
    upper = int(n ** (1 / 2)) + 1

    out = []

    for k in range(1, upper):
        if n % k == 0:
            out.append(k)

    return out

def get_square_size(size: int):
    """
    Finds a suitable square size for our chessboard
    """
    while not (divs := divisors(size)[1:-1]):
        size += 1

    return divs[-1]


def draw_checkboard_squares(
    squares_loc: list[svg.Point], square_size: int, color: str
) -> str:
    """
    Provides appropriate svg format text to draw our squares
    """
    out = [svg.genere_balise_debut_groupe("none", color, "none")]

    for square_loc in squares_loc:
        out.append(svg.genere_rectangle(square_loc, square_size, square_size))

    out.append(svg.genere_balise_fin_groupe())

    return "\n".join(out)


def main():
    _, raw_size, *_ = sys.argv

    size = int(raw_size)
    square_size = get_square_size(size)

    white_squares = []
    black_squares = []

    print(svg.genere_balise_debut_image(size, size))

    for i in range(size // square_size):
        for j in range(size // square_size):
            square_loc = svg.Point(i * square_size, j * square_size)
            if (i + j) % 2 == 0:
                white_squares.append(square_loc)
            else:
                black_squares.append(square_loc)

    print(draw_checkboard_squares(white_squares, square_size, "white"))
    print(draw_checkboard_squares(black_squares, square_size, "black"))

    print(svg.genere_balise_fin_image())


if __name__ == "__main__":
    main()
