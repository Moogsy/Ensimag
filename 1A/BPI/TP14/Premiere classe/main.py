#!/usr/bin/env python3

"""Un exemple de classe : point"""


class Point:
    """Un point dans le plan 2D.

    Un point possède une abscisse et une ordonnée.
    __str__ est une "fonction" spéciale, utilisée par l'interpréteur
    entre autre lorsqu'un point doit être affiché sur la sortie
    standard au travers d'un appel à la fonction print.
    """

    def __init__(self, x, y):
        self.abscisse = x
        self.ordonnee = y

    def __str__(self):
        return "{0.__class__.__name__}({0.x}, {0.y})".format(self)


def main():
    """Test de notre classe Point"""

    # Création de deux points
    point1 = Point(17, 23)
    point2 = Point(5, 7)

    # Affichage de la somme des abscisses
    # __str__ est automatiquement appelé par l'interpréteur
    # pour savoir comment afficher un point.
    somme1 = point1.abscisse + point2.abscisse
    print("Somme de l'abscisse de", point1,
          "et de l'abscisse de", point2, "=", somme1)

    # Les points sont modifiables.
    point1.abscisse = 3
    somme1 = point1.abscisse + point2.abscisse
    print("Somme de l'abscisse de", point1,
          "et de l'abscisse de", point2, "=", somme1)


if __name__ == "__main__":
    main()
