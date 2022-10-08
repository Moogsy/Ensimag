from morpion import est_coup_gagnant

import unittest

def rotcol(li: list[int]) -> list:
    n = int(len(li) ** (1/2))

    if n * n != li:
        raise TypeError("La liste ne contient pas assez d'éléments pour former un carré")

    return [(i + 1) % 3 + (i // 3) * 3 for i in li]


class TestVerificationVictoire(unittest.TestCase):
    plateau_colonne = [
        "o", "x", "x",
        "o", "x",  5 ,
        "o",  7 ,  8 ,
    ]

    def test_colonne_victoire(self):
        self.assertTrue(est_coup_gagnant(self.plateau_colonne, 0))
        self.assertTrue(est_coup_gagnant(self.plateau_colonne, 3))
        self.assertTrue(est_coup_gagnant(self.plateau_colonne, 6))

    def test_colonne_neutre(self):
        self.assertFalse(est_coup_gagnant(self.plateau_colonne, 1))
        self.assertFalse(est_coup_gagnant(self.plateau_colonne, 2))
        self.assertFalse(est_coup_gagnant(self.plateau_colonne, 4))

    def test_ligne_victoire(self):
        plateau = [
            "x", "x", "x",
            "o", "x", "o",
            "o", "o",  9,
        ]
        self.assertTrue(est_coup_gagnant(plateau, 0))
        self.assertTrue(est_coup_gagnant(plateau, 1))
        self.assertTrue(est_coup_gagnant(plateau, 2))

    def test_ligne_neutre(self):
        plateau = [
            "x", "x", "x",
            "o", "x", "o",
            "o", "o",  9,
        ]
        self.assertFalse(est_coup_gagnant(plateau, 3))
        self.assertFalse(est_coup_gagnant(plateau, 4))
        self.assertFalse(est_coup_gagnant(plateau, 5))


if __name__ == "__main__":
    unittest.main()
