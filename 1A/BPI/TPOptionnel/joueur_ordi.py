import random

def joue_coup(cases: list[int | str], symbole: str) -> int:
    """
    Joue un coup aléatoirement
    """
    cases_libres = [x for x in cases if x not in ('x', 'o')]
    return int(random.choice(cases_libres))

