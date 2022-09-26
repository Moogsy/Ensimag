from typing import Iterable

var1 = "123"
var2 = [1, 2, 3]
var3 = (1, 2, 3)
var4 = range(1, 4)
var5 = ["toto", range(3), ["t", "o", "t", "o"]]
var6 = ([1, 2, 3], [4, 5, 6])
var7 = [[[1, 2], [3, 4]], [[5, 6]]]


def affiche_unidimension(iterable: Iterable):
    """
    Affiche les éléments d'une structure à une dimension
    """
    for x in iterable:
        print(x)


def affiche_bidimension(iterables: Iterable):
    """
    Affiche les éléments d'une structure à deux dimensions
    """
    for iterable in iterables:
        affiche_unidimension(iterable)


def affiche_tridimension(sur_iterables: Iterable):
    """
    Affiche les éléments d'une structure à trois dimensions
    """
    for sur_iterable in sur_iterables:
        affiche_bidimension(sur_iterable)


def affiche_ndimension(iterable: Iterable):
    """
    Affiche les éléments d'une structure en dimension quelconque
    """
    for obj in iterable:
        try:
            iter(obj)
        except TypeError:  # L'objet n'est pas iterable
            print(obj)
        else:
            affiche_ndimension(obj)
