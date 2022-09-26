def get_side_length(length: int) -> int:
    n = int(len(li) ** (1/2))

    if n * n != len(li):
        raise TypeError("La liste ne contient pas assez d'éléments pour former un carré")

    return n


def rot_col(li: list[int], shift: int) -> list:
    """
    Shifts columns *shift* times to the left
    """
    n = get_side_length(len(li))

    return [(i + shift) % n + (i // n) * n for i in li]


li = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

breakpoint()