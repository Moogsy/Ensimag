#! /usr/bin/python3.10
import sys
import svg

LONGUEUR_CARRE = 40


def obtiens_taille_image() -> tuple[int, int]:
    """
    Attends et renvoie la taille d'image que l'utilisateur a demandée
    """
    _, longueur, largeur = sys.argv

    return svg.Dimensions(int(longueur), int(largeur))


def genere_carre(depuis: svg.Point, taille: int) -> list[str]:
    """
    Genere un carré à partir de son point situé en bas à gauche
    et de sa taille
    """
    points = [
        depuis,
        svg.Point(depuis.x + taille, depuis.y),
        svg.Point(depuis.x + taille, depuis.y - taille),
        svg.Point(depuis.x, depuis.y - taille),
    ]

    lignes = []

    for i, _ in enumerate(points):
        lignes.append(svg.genere_segment(points[i - 1], points[i]))

    return lignes


def genere_plateau(
    dimensions: svg.Dimensions,
    longueur_carre: int,
) -> list[str]:

    offset_x = 0
    offset_y = dimensions.largeur

    sortie = []

    num_carre = 1
    op = 1

    while True:
        while -longueur_carre <= offset_x + op * longueur_carre <= dimensions.longueur:
            point_actuel = svg.Point(offset_x, offset_y)
            sortie.extend(genere_carre(point_actuel, longueur_carre))
            sortie.append(svg.genere_texte(num_carre, point_actuel, couleur="red"))
            num_carre += 1

            offset_x += op * longueur_carre

        offset_x -= op * longueur_carre

        if offset_y - 2 * longueur_carre < 0:
            return sortie

        for i in range(2):

            offset_y -= longueur_carre

            point_actuel = svg.Point(offset_x, offset_y)

            sortie.extend(genere_carre(svg.Point(offset_x, offset_y), longueur_carre))
            if i == 0:
                sortie.append(svg.genere_texte(num_carre, point_actuel, couleur="red"))

        op *= -1
        num_carre += 1

    return sortie


def genere_cases(dimensions: svg.Dimensions) -> list[str]:
    """
    Genere les cases qui seront dessinées sur le plateau
    et renvoie une liste de lignes à dessiner
    """
    sortie = []

    sortie.extend(
        genere_plateau(
            dimensions,
            LONGUEUR_CARRE,
        )
    )

    return sortie


def main():
    dimensions = obtiens_taille_image()

    print(svg.genere_balise_debut_image(dimensions.longueur, dimensions.largeur))

    print(svg.genere_couleur_fond(dimensions.longueur, dimensions.largeur, "grey"))

    print("\n".join(genere_cases(dimensions)))

    print(svg.genere_balise_fin_image())


if __name__ == "__main__":
    main()
