def pivote(tableau: list[int], indice_pivot: int) -> tuple[list[int], list[int]]:
    """
    Renvoie deux tableaux, le premier contenant les éléments inférieurs
    de tableau[indice_pivot], le second contenant le reste

    Les complexité en temps et en espace sont toutes deux linéaires.
    """
    dessous = []
    dessus = []
    comparant = tableau[indice_pivot]

    for index, n in enumerate(tableau):
        if index == indice_pivot:
            continue
        elif n <= comparant:
            dessous.append(n)
        else:
            dessus.append(n)

    return dessous, dessus


def echange(tableau: list[int], indice_a: int, indice_b: int):
    """
    Echange deux éléments du tableau
    """
    tableau[indice_a], tableau[indice_b] = tableau[indice_b], tableau[indice_a]


def deplace_a_gauche_de(tableau: list[int], *, depuis: int, vers: int):
    """
    Deplace l'élément tableau[depuis] jusqu'à tableau[vers - 1], créant
    une case si nécessaire (pas d'indices négatifs)
    en conservant l'ordre des autres éléments puis renvoie le nouvel
    indice de tableau[depuis]

    On impose d'avoir depuis >= vers (en tenant compte des indice négatifs)
    """
    if depuis < 0:
        depuis = len(tableau) + depuis

    if vers < 0:
        vers = len(tableau) + vers

    while depuis > vers:
        echange(tableau, depuis, depuis - 1)
        depuis -= 1


def pivote_en_place(tableau: list[int], *, indice_pivot: int):
    """
    Partitionne le tableau en deux parties séparées par tableau[indice_pivot]
    la partie gauche contenant les éléments inférieurs au pivot, l'autre
    contenant les éléments strictement supérieurs

    Les complexités en espace et en temps dans le pire des cas sont linéaires.
    """
    echange(tableau, indice_pivot, 0)

    indice_pivot = 0
    pivot = tableau[indice_pivot]

    for index, elem in enumerate(tableau[1:], start=1):
        if elem <= pivot:
            deplace_a_gauche_de(tableau, depuis=index, vers=indice_pivot)
            indice_pivot += 1
