#! /usr/bin/python
"""
Utilitaire pour generer des images au format PGM
"""

import random
from typing import Any, Callable
from collections import namedtuple
from functools import reduce

Dimensions = namedtuple("Dimensions", "largeur longueur")
Point = namedtuple("Point", "x y")
Cercle = namedtuple("Cercle", "centre rayon")
Tableau = namedtuple("Tableau", "grille dimensions")


def distance_points_carre(point_1: Point, point_2: Point) -> int:
    """
    Renvoie la distance aucarré entre deux points
    """
    return (point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2


def affiche_entete(dim: Dimensions):
    """
    Affiche l'en-tête du fichier sur la sortie standard
    """
    print("P2")
    print(*dim, sep=" ")
    print(255)
    print()


def rayon_maximal(dimensions: Dimensions, point: Point) -> int:
    """
    Renvoie la distance au bord le plus proche d'un point
    (en ne tenant compte que des mouvements horizontaux et verticaux)
    """
    distance_bord_gauche = point.x
    distance_bord_droit = dimensions.longueur - point.x

    distance_bord_haut = point.y
    distance_bord_bas = dimensions.largeur - point.y

    return min(
        distance_bord_haut, distance_bord_bas, distance_bord_gauche, distance_bord_droit
    )


def tire_cercle(dimensions: Dimensions) -> Cercle:
    """
    Renvoie un cercle complètmeent situé à l'intérieur de l'image
    """
    dimension_x = random.randint(0, dimensions.longueur)
    dimension_y = random.randint(0, dimensions.largeur)

    centre = Point(dimension_x, dimension_y)
    distance_bord = rayon_maximal(dimensions, centre)

    if distance_bord == 0:
        rayon = 0

    rayon = random.randint(1, distance_bord)

    return Cercle(centre, rayon)


def genere_tableau(dimensions: Dimensions, defaut=255) -> Tableau:
    """
    Génère un tableau de points ayant la bonne dimensions
    """
    grille = [[defaut] * dimensions.longueur for _ in range(dimensions.largeur)]

    return Tableau(grille, dimensions)


def trouve_points_dans_cercle(dimensions: Dimensions, cercle: Cercle) -> Tableau:
    """
    Renvoie un tableau montrant quelles cases sont situées dans le cercle
    """
    rayon2 = cercle.rayon**2

    tableau_sortie = genere_tableau(dimensions, defaut=False)

    for i in range(dimensions.largeur):
        for j in range(dimensions.longueur):
            point = Point(i, j)

            if distance_points_carre(point, cercle.centre) <= rayon2:
                tableau_sortie.grille[i][j] = True

    return tableau_sortie


def map_tableaux(
    tableau_g: Tableau, tableau_d: Tableau, func: Callable[[Any, Any], Any]
) -> Tableau:
    """
    Crée un nouveau tableau élément par élémént en appellant la fonction func(x, y)
    sur chacun des éléments des deux tableaux fournis
    """
    if tableau_d.dimensions != tableau_g.dimensions:
        raise TypeError("Les deux tableaux n'ont pas la même dimension")

    tableau_sortie = genere_tableau(tableau_d.dimensions, defaut=False)

    for i in range(tableau_g.dimensions.largeur):
        for j in range(tableau_g.dimensions.longueur):
            tableau_sortie.grille[i][j] = func(
                tableau_g.grille[i][j], tableau_d.grille[i][j]
            )

    return tableau_sortie


def combine_masques(tableau_g: Tableau, tableau_d: Tableau) -> Tableau:
    """
    Combine plusieurs masques en un seul
    """
    return map_tableaux(tableau_g, tableau_d, lambda x, y: x or y)


def genere_couleurs(tableau: Tableau, masque: Tableau) -> Tableau:
    """
    Genere les couleurs pour le tableau
    """

    def choix_couleur(_: Point, est_dans_cercle: bool) -> int:
        """
        Remplis les couleurs si besoin
        """
        if est_dans_cercle:
            return random.randint(0, 255)
        else:
            return 255

    return map_tableaux(tableau, masque, choix_couleur)


def affiche_tableau(tableau: Tableau):
    """
    Affiche le tableau sur la sortie standard avec au format PGM
    """
    for ligne in tableau.grille:
        print(*ligne, sep=" ")


def main():
    """
    Point d'entrée de la fonction
    """
    largeur, longueur = input().split()
    dimensions = Dimensions(int(largeur), int(longueur))

    affiche_entete(dimensions)

    cercles = [
        tire_cercle(dimensions),
        tire_cercle(dimensions),
    ]

    masques = [trouve_points_dans_cercle(dimensions, cercle) for cercle in cercles]

    masque_total = reduce(combine_masques, masques)

    sortie = genere_tableau(dimensions, defaut=255)
    sortie = genere_couleurs(sortie, masque_total)

    affiche_tableau(sortie)


if __name__ == "__main__":
    main()
