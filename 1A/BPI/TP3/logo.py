"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

import math
import svg

AngleDegre = float


def avance(
    abscisse: float,
    ordonnee: float,
    direction: AngleDegre,
    crayon_en_bas: bool,
    distance: float,
) -> svg.Point:
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """

    depart = svg.Point(abscisse, ordonnee)

    direction_rad = direction * math.pi / 180

    arrivee = svg.Point(
        depart.x + distance * math.cos(direction_rad),
        depart.y - distance * math.sin(direction_rad),
    )

    if crayon_en_bas:
        print(svg.genere_segment(depart, arrivee))

    return arrivee


def fix_angle(angle: AngleDegre) -> AngleDegre:
    while angle < 0:
        angle += 360

    while angle > 360:
        angle -= 360

    return angle


def tourne_droite(direction: AngleDegre, angle: AngleDegre) -> AngleDegre:
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return fix_angle(direction - angle)


def tourne_gauche(direction: AngleDegre, angle: AngleDegre) -> AngleDegre:
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return fix_angle(direction + angle)
