#!/usr/bin/env python3

"""Un jeu de morpion"""

from typing import Literal
from types import ModuleType

# Les différents types de joueurs sont représentés par des modules.
# Les modules joueur_humain et joueur_ordi doivent être réalisés.
# Le module joueur_ordi_malin est fourni.
# Le module joueur_humain demande simplement à l'utilisateur de jouer.
# Le module joueur_ordi joue automatiquement. Sa stratégie n'est pas spécifiée.
import joueur_humain
import joueur_ordi
import joueur_ordi_malin

CaseMorpion = Literal["x", "o"] | int
Plateau = list[CaseMorpion]


def recupere_chaine_a_afficher(symbole: Literal["x", "o"]) -> str:
    """Renvoie la chaîne de caractère à afficher pour le symbole donné.

    Pour le symbole "x", le caractère unicode "MULTIPLICATION X", affiché
    en rouge doit être utilisé.
    Pour le symbole "o", le caractère unicode "WHITE CIRCLE", affiché
    en bleu doit être utilisé.

    précondition : symbole est soit "x" soit "o"
    """
    stop = "\033[0;0m"
    bleu = "\33[34m"
    rouge = "\33[31m"

    if symbole == "o":
        return bleu + "\u25cb" + stop
    elif symbole == "x":
        return rouge + "\u2715" + stop
    else:
        return symbole


def affiche_plateau(cases: Plateau):
    """Affiche le plateau représenté par la liste cases à 9 éléments.

    L'affichage se fait sur la sortie standard uniquement en utilisant
    des appels à la fonction print.

    précondition : chacune des cases contient soit
      - la chaîne de caractères "x" (case occupée par le joueur 1)
      - la chaîne de caractères "o" (case occupée par le joueur 2)
      - la chaîne de caractères "i" avec i entier correspondant au
        numéro de la case (case libre)
    précondition : cases est un tuple de 9 éléments
    """
    ligne_haut, ligne_milieu, ligne_bas = cases[:3], cases[3:6], cases[6:]

    print(*map(recupere_chaine_a_afficher, ligne_haut), sep=" | ")
    print("-" * 9)
    print(*map(recupere_chaine_a_afficher, ligne_milieu), sep=" | ")
    print("-" * 9)
    print(*map(recupere_chaine_a_afficher, ligne_bas), sep=" | ")
    print()


def est_coup_gagnant(cases: Plateau, coup: int) -> bool:
    """Verifie si le coup joué est gagnant.

    Renvoie True s'il l'est, False sinon.
    """
    # TODO: Les victoires ne sont pas détectées sur la 2e ligne
    colonne = coup % 3
    ligne = (coup // 3) * 3

    # On verifie si la colonne a 3 éléments identiques
    if cases[colonne] == cases[colonne + 3] == cases[colonne + 6]:
        return True

    # On verifie si la ligne a 3 elements identiques
    if cases[ligne] == cases[ligne + 1] == cases[ligne + 2]:
        return True

    # On vérifie si la diagonale sud-est est remplie
    if cases[0] == cases[4] == cases[8]:
        return True

    # On vérifie si la diagonale sud-ouest est remplie
    if cases[2] == cases[4] == cases[6]:
        return True

    return False


def joue_coup(
    joueur: ModuleType,
    joueur_num: Literal[1, 2],
    cases: list[CaseMorpion],
    symbole: CaseMorpion,
) -> Plateau:
    """Joue un coup.

    Cette fonction effectue les opérations suivantes tout en affichant
    ce qu'il se passe sur la sortie standard :
      - affiche le plateau représenté par cases
      - utilise le module joueur pour savoir quel coup doit être joué
      - met à jour le plateau de jeu avec ce coup
      - affiche le plateau et le numéro du joueur gagnant si c'est gagné
        puis quitte le programme
      - renvoie le nouveau plateau

    précondition : joueur est un module avec une fonction
                   joue_coup(cases, symbole) qui renvoie le
                   numéro d'une case précédemment inoccupée.
    précondition : joueur_num est soit l'entier 1 soit l'entier 2
    précondition : cases est une list de 9 éléments
    précondition : symbole est soit "x" soit "o"

    """
    affiche_plateau(cases)
    coup = joueur.joue_coup(cases, symbole)
    cases[coup] = symbole

    if est_coup_gagnant(cases, coup):
        affiche_plateau(cases)
        print(f"Le joueur {joueur_num} a gagné ({symbole})")
        exit(0)

    return cases


def joue_partie():
    """Joue une partie complète de morpion"""

    # Initialisation des deux joueurs en demandant à l'utilisateur
    # Parenthèses nécessaires pour "spliter un string literal"
    message_choix_joueur = (
        "Veuillez choisir le type du joueur {} en tapant\n"
        "  0 pour humain\n"
        "  1 pour un ordinateur\n"
        "  2 pour un ordinateur très malin\n"
        "  entrez votre choix : "
    )

    print(message_choix_joueur.format(1), end="")
    type1 = int(input())
    print(message_choix_joueur.format(2), end="")
    type2 = int(input())
    joueur1 = (
        joueur_humain
        if type1 == 0
        else (joueur_ordi if type1 == 1 else joueur_ordi_malin)
    )
    joueur2 = (
        joueur_humain
        if type2 == 0
        else (joueur_ordi if type2 == 1 else joueur_ordi_malin)
    )
    print()

    # Initialisation et affichage du plateau vide
    # Une case vide est représentée par son numéro,
    # utilisé par le joueur humain pour indiquer
    # quelle case il joue.
    cases = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Joue 9 coups au maximum
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")

    # Si on arrive là, il y a égalité
    print("Match nul !")


if __name__ == "__main__":
    joue_partie()
