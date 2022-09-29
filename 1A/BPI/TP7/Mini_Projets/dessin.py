"""Dessin 
"""

import random
import svg

def couleur_aleatoire() -> str:
    """
    Renvoie une couleur aléatoire valide au format svg
    """
    r, g, b = random.choices(range(255), k=3)
    return f"rgb({r}, {g}, {b})"


def affiche_triangle(triangle: svg.Triangle, couleur: str):
    """
    Affiche un triangle
    """
    fmt = '\n'.join([
        svg.genere_balise_debut_groupe(couleur, couleur, 1),
        svg.genere_balise_debut_groupe_transp(random.random()),
        svg.genere_polygone(triangle),
        svg.genere_balise_fin_groupe(),
        svg.genere_balise_fin_groupe(),
    ])
    print(fmt)
