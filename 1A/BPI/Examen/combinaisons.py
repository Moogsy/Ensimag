#!/usr/bin/env python3

"""Un programme qui ne sert à pas grand chose."""

import sys


def teste():
    """Teste les fonctions :
        - `recupere_combinaisons_2`
        - `renverse`
        - `recupere_combinaisons`
        - `recupere_parametres`

    Ces trois fonctions testées seront écrites plus tard, mais c'est
    souvent une bonne chose de commencer par les tests, donc allons-y.
    En plus, écrire ce test vous obligera à réfléchir à l'algorithme
    général à appliquer pour générer les combinaisons, sur des séquences
    simples.

    Les spécifications du travail à réaliser sont données en commentaire
    dans le corps de la fonction ci-dessous.
    Vous devez rajouter une ou plusieurs lignes de code à chaque fois
    qu'il y a un TODO suivi de trois points.
    Pensez à bien enlever ces TODO et ces trois points dès que vous les
    avez implémentés.
    Merci de respecter les spécifications À LA LETTRE pour que la
    correction automatique soit possible.

    Pour rappel, en Python une séquence `seq` est un objet sur lequel on
    peut :
      - utiliser la fonction `len(seq)` pour connaître sa taille. Cette
        opération s'effectue en temps constant ;
      - utiliser une boucle `for` pour parcourir ses éléments ;
      - accéder au ième élément avec `seq[i]` (le premier élément est à
        l'indice `0`).
    """

    print('Résultats calculés dans ma tête pour la séquence "ABCD" et k=2')
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence "ABCD" et k=2), avec une seule
    # combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple AC
    print(*["AB", "AC", "AD", "BC", "BD", "CD"], sep="\n")

    print('Résultats calculés par recupere_combinaisons_2("ABCD")')
    # effectue l'appel à recupere_combinaisons_2('ABCD'), puis affiche
    # sur la sortie standard les combinaisons renvoyées par cet appel,
    # avec une seule combinaison par ligne. Une combinaison étant un
    # tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print``, c'est à dire de ne faire aucun
    # formatage. La combinaison AC sera donc affichée de la façon
    # suivante : ('A', 'C')
    print(*recupere_combinaisons_2("ABCD"), sep="\n")

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultat de renverse sur [1, 2, 3]")
    # effectue l'appel à renverse([1, 2, 3]), puis
    # puis affiche sur ce résultat
    print(renverse([1, 2, 3]))

    # affiche sur la sortie standard une ligne vide
    print()

    print(
        "Résultats calculés dans ma tête pour la séquence [0, 1, 2, 3, 4] et k=3")
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence [0, 1, 2, 3, 4] et k=3), avec
    # une seule combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple 014
    print(*["012", "013", "014", "023", "024",
          "034", "123", "124", "134", "234"], sep="\n")

    print("Résultats calculés par recupere_combinaisons([0, 1, 2, 3, 4], 3)")
    # effectue l'appel à recupere_combinaisons([0, 1, 2, 3, 4], 3), puis
    # affiche sur la sortie standard les combinaisons renvoyées par cet
    # appel, avec une seule combinaison par ligne. Une combinaison étant
    # un tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print`, c'est à dire de ne faire aucun formatage.
    # La combinaison 014 sera donc affichée de la façon suivante : (0, 1, 4)
    print(*recupere_combinaisons([0, 1, 2, 3, 4], 3), sep="\n")

    # affiche sur la sortie standard une ligne vide
    print()

    # effectue l'appel recupere_parametres(x) avec x étant premier
    # argument de la ligne de commande puis affiche la séquence et
    # k renvoyés par cet appel.
    # Par exemple pour l'exécution de `python combinaisons.py input.txt`
    # x est `input.txt`
    print(
        "Résultats de recupere_parametres sur le fichier donné "
        "en paramètre sur la ligne de commande"
    )
    sequence,k = recupere_parametres(sys.argv[1])
    print(sequence)
    print(k)

    # affiche sur la sortie standard une ligne vide
    print()

    print(
        "Résultats calculés par recupere_combinaisons sur "
        "les paramètres dans le fichier"
    )
    # effectue l'appel à recupere_combinaisons en utilisant les paramètres
    # renvoyés par l'appel à recupere_parametres(x), puis affiche sur la
    # sortie standard les combinaisons renvoyées par cet appel, avec une
    # seule combinaison par ligne. Une combinaison étant un tuple, on vous
    # demande pour l'affichage de passer directement ce tuple à la fonction
    # `print`, c'est à dire de ne faire aucun formatage. La combinaison AC
    # sera donc affichée de la façon suivante : ('A', 'C')
    seq,k = recupere_parametres(sys.argv[1])
    print(*recupere_combinaisons(seq, k), sep="\n")


def recupere_parametres(filename: str) -> tuple[list, int]:
    """Renvoie un tuple à deux entrées contenant la séquence et
    le paramètre k, DANS CET ORDRE, lus à partir du fichier passé
    en paramètre.

    Spécifications PRÉCISES (pensons aux tests automatiques)
    sur le format du fichier :
       - la première ligne contient le nombre k
       - les lignes suivantes contiennent les éléments de la séquence

    Vous trouverez un fichier `input.txt` dans votre dossier `exam` à
    titre d'exemple.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

    k, *sequence = lines

    return (sequence,int(k))


def recupere_combinaisons_2(sequence: list[str]) -> list[tuple[str, str]]:
    """ "Renvoie toutes les combinaisons de taille 2 de la séquence donnée.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par une
         `list` de `tuple`.
    """
    sortie = []

    for index, symbole_g in enumerate(sequence):
        for symbole_d in sequence[index+1:]:
            sortie.append((symbole_g, symbole_d))

    return sortie


def renverse(sequence):
    """
    Renvoie une nouvelle `list` contenant tous les éléments
    de la séquence donnée en paramètre mais dans l'ordre inverse.
    """
    return list(reversed(sequence))


def powerset_k(sequence: list, k: int):
    """
    Même fonctionnalité que combinaison, mais en renvoyant
    une liste de listes au lieu d'avoir des tuples
    """
    out = [[]]

    if k == 0:
        return out

    for index, elem in enumerate(sequence):
        for subseq in powerset_k(sequence[index+1:], k-1):
            if len(subseq) + 1 == k:
                out.append([elem] + subseq)

    if k > 0:
        out = out[1:]

    return out


def recupere_combinaisons(sequence: list, k: int):
    """
    Renvoie toutes les combinaisons de taille k de la sequence donnée.

    Attention, cette fonction est difficile à implémenter.
    Il est vivement conseillé de réfléchir à un algorithme sur le
    papier avant de se lancer dans le code.
    Vous pouvez utiliser la fonction `renverse` si besoin,
    mais ce n'est pas du tout une obligation.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par
         une `list` de `tuple`.
    """
    return [tuple(x) for x in powerset_k(sequence, k)]

def affiche_nombre_combinaisons():
    """Affiche le nombre de k-combinaisons d'une séquence de taille n.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - l'affichage se fera en fonction de n, la taille de la séquence,
         et du paramètre k
       - les seuls caractères autorisées dans la chaîne affichée sont :
           + `*`, `/` et `-`
           + les lettres `n` et `k`
           + des parenthèses
           + le caractère `!` (factorielle)
    """
    print("n! / (k! * (n-k)!)")


# La fonction teste() est appelée uniquement dans
# le cas où le programme est invoqué comme programme
# principal avec `python combinaisons.py input.txt`
# ou avec `./combinaisons.py input.txt`
if __name__ == "__main__":
    teste()
