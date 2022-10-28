#!/usr/bin/env python3

"""Listes simplements chainees + quelques operations"""

from typing import Any, Generator, NoReturn, Optional
import traceur


class Cellule:
    """Une cellule d'une liste."""
    def __init__(self, valeur: Any, suivant: Optional["Cellule"] = None):
        self.valeur = valeur
        self.suivant = suivant

    def __repr__(self):
        return "{0.__class__.__name__}({0.valeur}, {0.suivant})".format(self)

    __str__ = __repr__

class ListeSimplementChainee:
    """Une liste simplement chainee."""
    def __init__(self, tete: Cellule | None = None) -> None:
        self.tete = self.queue = tete

        if tete is None:
            self.taille = 0
        else:
            self.taille = 1

    def __repr__(self):
        return "{0.__class__.__name__}({0.tete})".format(self)

    def __str__(self):
        return "{0.__class__.__name__}<tete={0.tete}>, <queue={0.queue}>, <longueur=<{0.taille}>)".format(self)

    def __len__(self):
        return self.taille

    def __getitem__(self, val: int) -> Any:

        if val < 0:
            val = len(self) - val

        for index, cell in enumerate(self):
            if index == val:
                return cell

        raise IndexError("List index out of range")

    def __iter__(self) -> Generator[Cellule, None, None]:
        cellule = self.tete

        while cellule is not None:
            yield cellule

            cellule = cellule.suivant

    def ajoute_en_tete(self, valeur: Any):
        """Ajoute une cellule en tete"""

        self.taille += 1
        cellule = Cellule(valeur, self.tete)

        if self.tete is None:
            self.tete = self.queue = cellule
        else:
            self.tete = cellule

    def ajoute_en_queue(self, valeur: Any):
        """Ajoute une cellule en queue."""
        self.taille += 1

        nouvelle_queue = Cellule(valeur, None)

        if self.queue is None:
            self.ajoute_en_tete(valeur)
        else:
            self.queue.suivant = nouvelle_queue
            self.queue = nouvelle_queue

    def recupere_cellules(self):
        """Renvoie un vecteur contenant toutes les cellules de la liste_chainee"""
        return list(self)

    def recherche(self, valeur: Any) -> Any | None:
        """Recherche une valeur dans la liste_chainee donnée.

        Renvoie la premiere cellule contenant la valeur donnée ou
        None si la valeur n'est pas trouvée dans la liste_chainee.
        """
        for cellule in self:
            if cellule.valeur == valeur:
                return cellule

        return None

    def supprime(self, valeur):
        """Enleve la premiere cellule contenant la valeur donnée."""
        if self.tete is not None and self.tete.valeur == valeur:
            self.tete = self.tete.suivant

        for cellule in self:
            if cellule.suivant and cellule.suivant.valeur == valeur:
                cellule.suivant = cellule.suivant.suivant

                if cellule.suivant is None:
                    self.queue = cellule


def tli():
    li = ListeSimplementChainee()

    li.ajoute_en_tete(4)
    li.ajoute_en_tete(3)
    li.ajoute_en_tete(2)
    li.ajoute_en_tete(1)

    print(li[2])




def test_listes():
    """On teste les operations de base, dans differentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_0"
    )
    liste_chainee.ajoute_en_tete(3)
    liste_chainee.ajoute_en_tete(5)
    liste_chainee.ajoute_en_tete(2)
    liste_chainee.ajoute_en_tete(4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_1"
    )
    print("recherche : ", liste_chainee.recherche(3).valeur)
    liste_chainee.supprime(5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_2"
    )
    liste_chainee.supprime(4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_3"
    )

if __name__ == "__main__":
    tli()

