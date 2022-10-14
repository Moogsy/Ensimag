import itertools

from collections import Counter
import unittest
import main


def li_eq(li1: list, li2: list) -> bool:
    """
    On vérifie que:
    - Les listes contiennent les mêmes éléments
    - et que ces éléments sont présents en même quantité.
    """
    return Counter(li1) == Counter(li2)


class Tests(unittest.TestCase):
    def test_partition_elements_distincts_deja_trie(self):
        """
        Vérifie que la fonction pivote génère le bon résultat lorsque
        tous les éléments sont distincts et le tableau d'entrée déjà trié.
        On ne prend pas en compte l'ordre des éléments comme le veut
        l'énoncé.
        """
        li = [1, 2, 3, 4, 5]
        leq, ge = main.pivote(li, 2)

        assert li_eq(li[:2], leq)
        assert li_eq(li[3:], ge)

    def test_partition_deja_trie(self):
        """
        Vérifie que la fonction pivote génère le bon résultat lorsque
        le tableau d'entrée déjà trié.
        On ne prend pas en compte l'ordre des éléments comme le veut
        l'énoncé.
        """
        li = [1, 2, 2, 2, 2, 3, 4, 5]
        leq, ge = main.pivote(li, 2)

        assert li_eq([1, 2, 2, 2], leq)
        assert li_eq([3, 4, 5], ge)

    def test_partition_distincts_non_trie(self):
        """
        Vérifie que la fonction pivote génère le bon résultat lorsque les
        éléments sont dans un ordre quelque et non nécessairement distincts.
        On ne prend pas en compte l'ordre des éléments comme le veut
        l'énoncé.
        """
        li = [42, 1, 2, 3, 5, 6, 0, -1]
        leq, ge = main.pivote(li, 3)

        assert li_eq(leq, [1, 2, 0, -1])
        assert li_eq(ge, [42, 5, 6])

    def test_partition_non_trie(self):
        """
        Vérifie que la fonction pivote génère le bon résultat lorsque les
        éléments sont dans un ordre quelque et non nécessairement distincts.
        On ne prend pas en compte l'ordre des éléments comme le veut
        l'énoncé.
        """
        li = [42, 1, 2, 2, 2, 3, 5, 5, 6, 0, -1]
        leq, ge = main.pivote(li, 3)

        assert li_eq(leq, [1, 2, 2, 0, -1])
        assert li_eq(ge, [3, 5, 5, 6, 42])

    def test_deplacement_fin(self):
        """
        Test de la fonction deplace_a_droite_de lorsque le pivot se trouve
        a la fin
        """
        li = [1, 2, 3, 4]
        main.deplace_a_gauche_de(li, depuis=3, vers=0)
        self.assertEqual(li, [4, 1, 2, 3])

    def test_deplacement_normal(self):
        """
        test de la fonction deplace_a_droite_de lorsque ni
        l'élément source, ni l'élément destination
        ne se trouvent sur les bords
        """
        li = [1, 2, 3, 4, 5, 6]
        main.deplace_a_gauche_de(li, depuis=4, vers=1)
        self.assertEqual(li, [1, 5, 2, 3, 4, 6])

    def test_deplacement_nul(self):
        """
        Test de la fonction deplace_a_droite_de lorsque
        le pivot se trouve déjà à la fin
        """
        li = [1, 2, 3, 4]
        main.deplace_a_gauche_de(li, depuis=-1, vers=-1)
        self.assertEqual(li, [1, 2, 3, 4])

    def test_pivot_deja_trie(self):
        """
        Verifie que le pivot partitionne correctement la liste
        lorsqu'elle est déjà triée
        """
        li = [1, 2, 3, 4]

        main.pivote_en_place(li, indice_pivot=2)

        leq, ge = main.pivote(li, li.index(3))

        assert li_eq(leq, [1, 2]), leq
        assert li_eq(ge, [4]), ge

    def test_pivot(self):
        """
        Vérifie la fonction pivot dans un scénario quelconque
        """
        li = [1, 5, 3, 3, 5, 9, 0, -1, 2]
        main.pivote_en_place(li, indice_pivot=2)

        leq, ge = main.pivote(li, li.index(3))

        assert li_eq(leq, [1, 3, 0, -1, 2]), leq
        assert li_eq(ge, [5, 5, 9]), ge


if __name__ == "__main__":
    unittest.main()
