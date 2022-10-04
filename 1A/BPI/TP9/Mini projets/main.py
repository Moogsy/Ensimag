#!/usr/bin/python3

import sys
from typing import Generator, Literal


def signe(n: int) -> Literal[-1, 1] | None:
    """
    Renvoie le signe du nombre passé en argument,
    renvoie None s'il est nul.
    """
    try:
        return n // abs(n)
    except ZeroDivisionError:
        return None


def sous_suites_monotones(
    source: Generator[int, None, None]
) -> Generator[list[int], None, None]:
    """
    Crée un génératuer fournissant toutes les sous suite
    monotones à partir de la suite du générateur source

    Dans le cas où 0 ou 1 nombre est fourni, la séquence
    fournie sera directement renvoyée
    """
    tmp = []
    try:
        tmp.append(next(source))
        tmp.append(next(source))
    except StopIteration:
        yield tmp
        return

    monotonie_actuelle = signe(tmp[1] - tmp[0])

    for num in source:
        nouvelle_monotonie = signe(num - tmp[-1])

        if nouvelle_monotonie == monotonie_actuelle or nouvelle_monotonie is None:
            tmp.append(num)
        else:
            yield tmp

            tmp = [tmp[-1], num]
            monotonie_actuelle = nouvelle_monotonie

    yield tmp


def plus_grande_sous_suite_monotone(source: Generator[int, None, None]) -> list[int]:
    """
    Renvoie la plus grande sous suite monotone du générateur source
    """
    return max(sous_suites_monotones(source), key=len, default=[])


def lis_nombres(fname: str) -> Generator[int, None, None]:
    """
    Extrait les nomres du fichier demandé.
    """
    with open(fname, "r", encoding="utf-8") as file:
        for line in file:
            for num in line.split():
                yield int(num)


def main():
    """
    Extrait la suite de nombre du fichier passé en argument de ligne de commande
    et affiche sa plus longue sous séquence monotone.

    En notant n le nombre de chiffre passé en argument:

    - la complexité en temps est O(n)
    - la complexité en mémoire est dans le pire des cas O(n)
    """
    _, fname, *_ = sys.argv

    suite = plus_grande_sous_suite_monotone(lis_nombres(fname))
    print(*suite, sep=" ")


if __name__ == "__main__":
    main()
