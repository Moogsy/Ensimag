#!/usr/bin/python3

import sys
from itertools import takewhile
from typing import Iterable, Literal


def signe(n: int) -> Literal[-1, 1] | None:
    """
    Renvoie le signe du nombre passé en argument,
    renvoie None s'il est nul.
    """
    try:
        return n // abs(n)
    except ZeroDivisionError:
        return None


def derniers_elements_egaux(sous_suite: list[int]) -> int:
    """
    Renvoie les derniers elements égaux de la 
    liste fournie qui doit déjà être triée.
    """
    dernier = sous_suite[-1]
    elements_egaux = [dernier]

    for x in reversed(sous_suite[:-1]):
        if x == dernier:
            elements_egaux.append(x)
        else:
            return elements_egaux

    return elements_egaux

def sous_suites_monotones(
    source: Iterable[int],
) -> Iterable[list[int]]:
    """
    Crée un génératuer fournissant toutes les sous suite
    monotones à partir de la suite du générateur source

    Dans le cas où 0 ou 1 nombre est fourni, la séquence
    fournie sera directement renvoyée
    """
    sous_suite = []
    try:
        sous_suite.append(next(source))
        sous_suite.append(next(source))
    except StopIteration:
        yield sous_suite
        return

    monotonie = signe(sous_suite[1] - sous_suite[0])

    for num in source:
        nouvelle_monotonie = signe(num - sous_suite[-1])

        if nouvelle_monotonie == monotonie or nouvelle_monotonie is None:
            sous_suite.append(num)
        else:
            yield sous_suite

            sous_suite = derniers_elements_egaux(sous_suite) + [num]
            monotonie = nouvelle_monotonie

    yield sous_suite


def plus_grande_sous_suite_monotone(source: Iterable[int]) -> list[int]:
    """
    Renvoie la plus grande sous suite monotone du générateur source
    """
    return max(sous_suites_monotones(source), key=len, default=[])


def lis_nombres(fname: str, **kwargs) -> Iterable[int]:
    """
    Renvoie un générateur fournissant les nombres contenus dans
    fichier dont le nom a été passé en argument
    """
    with open(fname, "r", **kwargs) as file:
        for line in file:
            for num in line.split():
                yield int(num)


def main():
    """
    Extrait la suite de nombre du fichier passé en argument de ligne de
    commande et affiche sa plus longue sous séquence monotone.

    En notant n le nombre de chiffre passé en argument:

    - la complexité en temps est O(n)
    - la complexité en mémoire est dans le pire des cas O(n)
    """
    _, fname, *_ = sys.argv

    source_nombres = lis_nombres(fname, encoding="utf-8")
    # suite = plus_grande_sous_suite_monotone(source_nombres)
    # print(*suite, sep=" ")

    print(*plus_grande_sous_suite_monotone(source_nombres), sep=" ")


if __name__ == "__main__":
    main()
