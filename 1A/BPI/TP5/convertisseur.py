#! /usr/bin/python

import svg


def lecture_points() -> list[svg.Point]:
    """
    Lis les points dans le fichier fournis
    """
    pts = []
    temp = []

    while True:
        try:
            coord = input()
        except EOFError:
            break

        temp.append(coord)

        if len(temp) == 2:
            x, y = temp  # type: ignore
            temp.clear()
            pts.append(svg.Point(int(x), int(y)))

    return pts


points = lecture_points()

print(svg.genere_balise_debut_image(640, 480))

print(
    svg.genere_balise_debut_groupe(
        couleur_ligne="black", couleur_remplissage="pink", epaisseur_ligne=2
    )
)

for point in points:
    print(
        svg.genere_cercle(point, 10)
    )

print(svg.genere_balise_fin_groupe())

print(svg.genere_balise_fin_image())
