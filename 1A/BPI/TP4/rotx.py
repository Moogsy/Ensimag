"""Module d'encodage/décodage par rotation"""


def rot(decalage: int, lettre: str) -> str | None:
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    if len(lettre) != 1 or not lettre.isalnum():
        return None

    est_majuscule = lettre.isupper()
    lettre = lettre.lower()

    debut_alphabet = ord("a")
    fin_alphabet = ord("z")

    position_alphabet = ord(lettre) - debut_alphabet
    position_decalee = position_alphabet + decalage

    nouvelle_position_alphabet = position_decalee % (fin_alphabet - debut_alphabet + 1)

    nouvelle_lettre = chr(nouvelle_position_alphabet + debut_alphabet)

    if est_majuscule:
        return nouvelle_lettre.upper()

    return nouvelle_lettre


def rot13(lettre: str) -> str:
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    return rot(13, lettre)
