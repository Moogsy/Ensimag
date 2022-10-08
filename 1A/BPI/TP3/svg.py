"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

VERSION = "1.1"
NAMESPACE = "http://www.w3.org/2000/svg"

AngleRadians = float
Dimensions = namedtuple("Dimensions", "longueur largeur")

Point = namedtuple("Point", "x y")
Segment = namedtuple("Segment", "p1 p2")
Triangle = namedtuple("Triangle", "p1 p2 p3")
Carre = namedtuple("Carre", "p1 p2 p3 p4")
Polygone = list[Point]


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_image(longueur: int, largeur: int):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    return f"<svg xmlns='{NAMESPACE}' version='{VERSION}' width='{longueur}' height='{largeur}'>"


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    return "</svg>"


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(
    couleur_ligne: str, couleur_remplissage: str, epaisseur_ligne: float
) -> str:
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return (
        f"<g stroke='{couleur_ligne}' stroke-width='{epaisseur_ligne}' "
        f"fill='{couleur_remplissage}'>"
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    return "</g>"


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre: Point, rayon: float) -> str:
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    return f"<circle cx='{centre.x}' cy='{centre.y}' r='{rayon}' />"


def genere_segment(dep: Point, arr: Point) -> str:
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    return f"""<line x1="{dep.x}" y1="{dep.y}" x2="{arr.x}" y2="{arr.y}" style="stroke: black;"/>"""


def genere_balise_debut_groupe_transp(niveau_opacite: float):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    """
    return f"<g opacity='{niveau_opacite}'>"


def _fmt_polygone(points: Polygone) -> str:
    """
    Renvoie la chaine de caractères formattants les points
    pour former un polygone
    """
    return " ".join([f"{x}, {y}" for x, y in points])


def genere_polygone(points: Polygone) -> str:
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableaux de points.
    """
    fmt = _fmt_polygone(points)
    return f"<polygon points='{fmt}' />"


def genere_couleur_fond(largeur_image: int, longueur_image: int, couleur: str) -> str:
    """
    Génère un rectangle permettant de changer la couleur de fond de l'image
    """
    points = [
        Point(0, 0),
        Point(0, longueur_image),
        Point(largeur_image, longueur_image),
        Point(largeur_image, 0),
    ]
    fmt = _fmt_polygone(points)

    return f"<polygon points='{fmt}' fill='{couleur}' />"


def genere_bordure_polygone(polygone: Polygone) -> list[str]:
    """
    Renvoie une liste de lignes permettant de tracer les bordures
    d'un polygone
    """
    sortie = []

    for i in range(len(polygone)):
        sortie.append(genere_segment(polygone[i - 1], polygone[i]))

    return sortie


def genere_bordure_carre(lieu: Point, taille: int) -> list[str]:
    """
    Génère un carré dont le point en haut à gauche sera situé
    aux coordonées "lieu" et dont les côtés auront pour longueur
    "taille".
    """
    points = [
        lieu,
        Point(lieu.x, lieu.y + taille),
        Point(lieu.x + taille, lieu.y + taille),
        Point(lieu.x + taille, lieu.y),
    ]

    return genere_bordure_polygone(points)


def genere_texte(texte: str, lieu: Point, *, couleur: str) -> str:
    """
    genere du texte au lieu choisi et ayant la couleur choisie.
    """
    return f"<text x='{lieu.x}' y='{lieu.y}' fill='{couleur}' > {texte} </text>"


def genere_rectangle(top_left: Point, width: int, height: int) -> str:
    """
    Retourne la chaîne de caractères corresponadant à un élément SVG représentant un rectangle.
    """
    x, y = top_left
    return f"<rect x='{x}' y='{y}' width='{width}' height='{height}'/>"

