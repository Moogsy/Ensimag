import unittest
from rotx import rot

class TestRotx(unittest.TestCase):
    def test_shift_one_lower(self):
        self.assertEqual(rot(1, "a"), "b")

    def test_shift_one_upper(self):
        self.assertEqual(rot(1, "A"), "B")

    def test_shift_multiple_lower(self):
        self.assertEqual(rot(5, "a"), "f")

    def test_shift_multiple_upper(self):
        self.assertEqual(rot(5, "A"), "F")

    def test_wrap_one_lower(self):
        self.assertEqual(rot(1, "z"), "a")

    def test_wrap_one_upper(self):
        self.assertEqual(rot(1, "Z"), "A")

    def test_wrap_multiple_lower(self):
        self.assertEqual(rot(4, "z"), "d")

    def test_wrap_multiple_upper(self):
        self.assertEqual(rot(4, "Z"), "D")

    def test_fullwrap_lower(self):
        self.assertEqual(rot(26, "k"), "k")

    def test_fullwrap_upper(self):
        self.assertEqual(rot(26, "J"), "J")


if __name__ == "__main__":
    unittest.main()
