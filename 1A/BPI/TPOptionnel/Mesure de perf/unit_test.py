import unittest
import random

from main import insert_sort, merge_sort, select_sort


class TestTris(unittest.TestCase):
    def test_tri_insertion_deja_trie(self):
        li = [*range(10)]
        insert_sort(li)
        self.assertEqual(li, [*range(10)])

    def test_tri_insertion_trie_decroissant(self):
        li = [*range(10)]
        li.reverse()
        insert_sort(li)
        self.assertEqual(li, [*range(10)])

    def test_tri_insertion_elements_distincts(self):
        li = [3, 5, 4, 2, 1]
        insert_sort(li)
        self.assertEqual(li, [1, 2, 3, 4, 5])

    def test_tri_insertion_quelconque(self):
        li = [2, 5, 6, 2, 7, 9, 20, 34]

        li2 = li.copy()
        li2.sort()

        insert_sort(li)

        self.assertEqual(li, li2)

    def test_tri_insertion_listes_aleatoires(self):
        """Test non biaisé
        Détection éventuelle de cas limites non testés précédemment
        """
        for _ in range(100):
            li_size = random.randint(1, 100)
            to_sort = random.choices(range(50), k=li_size)

            ref = to_sort.copy()
            ref.sort()

            insert_sort(to_sort)

            self.assertEqual(ref, to_sort)

    def test_tri_fusion_deja_trie(self):
        li = [*range(10)]
        li = merge_sort(li)
        self.assertEqual(li, [*range(10)])

    def test_tri_fusion_trie_decroissant(self):
        li = [*range(10)]
        li.reverse()
        li = merge_sort(li)
        self.assertEqual(li, [*range(10)])

    def test_tri_fusion_elements_distincts(self):
        li = [3, 5, 4, 2, 1]
        li = merge_sort(li)
        self.assertEqual(li, [1, 2, 3, 4, 5])

    def test_tri_fusion_quelconque(self):
        li = [2, 5, 6, 2, 7, 9, 20, 34]

        li2 = li.copy()
        li2.sort()

        li = merge_sort(li)

        self.assertEqual(li, li2)

    def test_tri_fusion_listes_aleatoires(self):
        """Test non biaisé
        Détection éventuelle de cas limites non testés précédemment
        """
        for _ in range(100):
            li_size = random.randint(1, 100)
            to_sort = random.choices(range(50), k=li_size)

            ref = to_sort.copy()
            ref.sort()

            to_sort = merge_sort(to_sort)

            self.assertEqual(ref, to_sort)


if __name__ == "__main__":
    unittest.main()
