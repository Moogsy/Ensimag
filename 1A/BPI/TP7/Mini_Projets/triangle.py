#!/usr/bin/env python3

import random
from math import cos, sin
from svg import Point, Triangle, AngleRadians


def triangle_aleatoire(
    range_largeur: tuple[float, float], range_longueur: tuple[float, float]
) -> Triangle:
    """
    Renvoie trois points aléatoires formant un triangle
    """
    largeur_min, largeur_max = map(int, range_largeur)
    longueur_min, longueur_max = map(int, range_longueur)

    abscisses = random.choices(range(largeur_min, largeur_max + 1), k=3)
    ordonnees = random.choices(range(longueur_min, longueur_max + 1), k=3)
    points = [Point(x, y) for x, y in zip(abscisses, ordonnees)]

    return Triangle(*points)


def tourne_triangle_autour(
    triangle: Triangle, centre: Point, angle: AngleRadians
) -> Triangle:
    """
    Trourne un triangle autour du centre d'un angle demandé
    """
    return Triangle(*[
            Point(
                (x - centre.x) * cos(angle) - (y - centre.y) * sin(angle) + centre.x,
                (x - centre.x) * sin(angle) + (y - centre.y) * cos(angle) + centre.y,
            )
            for x, y in triangle
    ])

