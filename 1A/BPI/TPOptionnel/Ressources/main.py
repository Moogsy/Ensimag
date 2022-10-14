#!/usr/bin/env python3
"""Manipulations complexes de tableaux dynamiques : listes d'intervalles"""

from collections import namedtuple

# Un ensemble de ressource est représenté par un intervalle et le nombre total
# de ressources qu'il peut contenir.
# Concernant la façon de définir les attributs de notre namedtuple,
# le code ci-dessous est correct car la documentation de la fonction
# collections.namedtuple dit :
#   "The field_names are a sequence of strings such as ['x', 'y'].
#     Alternatively, field_names can be a single string with each
#     fieldname separated by whitespace **and/or** commas,
#     for example 'x y' or 'x, y'."
EnsembleRessources = namedtuple("EnsembleRessources", "intervalles, nb_ressources")


def cree_ensemble_ressource(nb_ressources: int) -> EnsembleRessources:
    """Créé un ensemble de ressources de taille nb_ressources.

    L'ensemble est représenté par un namedtuple EnsembleRessources.

    L'ensemble créé contient toutes les ressources avec un identifiant id
    tel que 0 <= id < nb_ressources.
    """
    return EnsembleRessources([[0, nb_ressources]], nb_ressources)


def contient(ensemble_ressources: EnsembleRessources, identifiant: int) -> bool:
    """Test d'appartenance d'une ressource à un ensemble.

    Renvoie True si la ressource identifiée par l'identifiant donné
    est contenu dans ensemble_ressources et False sinon.
    """
    for intervalle in ensemble_ressources.intervalles:
        debut, fin = intervalle
        if identifiant in range(debut, fin):
            return True
    
    return False


def get_chaine(ensemble_ressources: EnsembleRessources):
    """Renvoie une chaîne de caractère représentant l'ensemble donné".

    Par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
    et que les ressources 0, 3, 4, 5, 6 et 7 sont contenues dans l'ensemble.
    """
    fmt = ["."] * ensemble_ressources.nb_ressources

    for intervalle in ensemble_ressources.intervalles:
        debut, fin = intervalle
        for i in range(debut, fin):
            fmt[i] = "x"

    return f"|{''.join(fmt)}|"


def ajoute(ensemble_ressources: EnsembleRessources, ensemble_ressources_a_ajouter: EnsembleRessources):
    """Ajoute des ressources précédemment enlevées dans un ensemble.

    Ajoute toutes les ressources de ensemble_ressources_a_ajouter dans
    l'ensemble ensemble_ressources.

    Le fait que les ressources ajoutées aient été précédemment enlevées
    implique qu'aucune des ressources à ajouter ne soit déjà présente dans
    ensemble_ressources.

    Enfin, les deux ensembles de ressources ont le même nb_ressources et les
    tableaux dynamiques d'intervalles de ces deux ressources sont triés.
    """
    ensemble_ressources.intervalles.extend(ensemble_ressources_a_ajouter.intervalles)
    ensemble_ressources.intervalles.sort()


def longueur_intervalle(intervalle: list[int]) -> int:
    """
    Renvoie la longueur de l'intervalle d'entiers [a, b)
    """
    debut, fin = intervalle
    return fin - debut

def enleve(ensemble_ressources: EnsembleRessources, nb_ressources: int):
    """Enlève nb_ressources de l'ensemble donnée.

    Les ressources enlevées sont les nb_ressources *premières ressources* de
    l'ensemble donné.

    Cette fonction *doit renvoyer* un nouvel ensemble de ressources de même
    taille que l'ensemble donné contenant uniquement les ressources qui ont
    été enlevées.
    """
    nb_ressources += ensemble_ressources.intervalles[0][0]

    a_renvoyer = []

    for index, intervalle in enumerate(ensemble_ressources.intervalles):
        debut, fin = intervalle

        if fin <= nb_ressources:
            a_renvoyer.append(ensemble_ressources.intervalles.pop(index))

        elif debut <= nb_ressources < fin:
            intervalle[0] = nb_ressources

            nv_intervalle = [debut, nb_ressources]
            a_renvoyer.append(nv_intervalle)

    return EnsembleRessources(a_renvoyer, ensemble_ressources.nb_ressources)


def test():
    """On teste en gruyerisant un ensemble de ressources"""
    ressources_disponibles = cree_ensemble_ressource(10)
    print(
        "Disponibles après création d'un ensemble à 10 éléments     :",
        get_chaine(ressources_disponibles),
    )
    ressources_reservees = [enleve(ressources_disponibles, c) for c in (2, 2, 3, 2, 1)]
    print(
        "Disponibles après 5 appels à enlève pour un total de 10    :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[1])
    print(
        "Disponibles après appel à ajout avec ressources 2 et 3     :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[3])
    print(
        "Disponibles après appel à ajout avec ressources 7 et 8     :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Reservees renvoyées par appel à enlève 3 sur disponibles   :",
        get_chaine(enleve(ressources_disponibles, 3)),
    )
    print(
        "Disponibles après le même appel à enlève 3                 :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Les intervalles de disponibles avec uniquement ressource 8 :",
        ressources_disponibles.intervalles,
    )


if __name__ == "__main__":
    test()
