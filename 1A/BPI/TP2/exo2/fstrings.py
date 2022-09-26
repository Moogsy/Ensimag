"""Illustration des f-strings"""


def convertit_point_en_chaine(x: float, y: float) -> str:
    """
    Convertit un point (x, y) en chaine de caractère
    """
    return f"({x}, {y})"


def test():
    assert convertit_point_en_chaine(1, 2) == "(1, 2)"
    assert convertit_point_en_chaine(3.5, 6.2) == "(3.5, 6.2)"

    print("Test ok")


if __name__ == "__main__":
    test()

