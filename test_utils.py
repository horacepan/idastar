import unittest
from utils import *

class TestUtils(unittest.TestCase):
    def test_even_perm(self):
        perm = [1, 2, 3, 4]
        self.assertTrue(even_perm(perm))

        perm = [1, 3, 2, 4]
        self.assertFalse(even_perm(perm))

        perm = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(even_perm(perm))

        perm = [1, 2, 3, 4, 5, 9, 7, 8, 6]
        self.assertFalse(even_perm(perm))

        perm = [1, 2, 3, 4, 9, 5, 8, 7, 6]
        self.assertFalse(even_perm(perm))

        perm = [1, 2, 3, 4, 9, 5, 8, 6, 7]
        self.assertTrue(even_perm(perm))

    def test_n_inversions(self):
        perm = [1, 2, 3, 4]
        self.assertEqual(n_inversions(perm), 0)

        perm = [1, 2, 3, 4, 9, 5, 8, 6, 7]
        self.assertEqual(n_inversions(perm), 6)

        perm = [1, 2, 3, 4, 9, 5, 8, 7, 6]
        self.assertEqual(n_inversions(perm), 7)

    def test_solveable(self):
        perm_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(solveable(perm_state))

        perm_state = [1, 2, 3, 4, 5, 9, 7, 8, 6]
        self.assertTrue(solveable(perm_state))

        perm_state = [1, 2, 3, 4, 5, 6, 7, 9, 8]
        self.assertTrue(solveable(perm_state))

        perm_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertTrue(solveable(perm_state))

        perm_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16]
        self.assertFalse(solveable(perm_state))

        perm_state = [13, 2, 10, 3, 1, 12, 8, 4, 5, 16, 9, 6, 15, 14, 11, 7]
        self.assertTrue(solveable(perm_state))

        perm_state = [13, 2, 10, 3, 1, 12, 8, 4, 5, 16, 9, 6, 15, 14, 11, 7]
        self.assertTrue(solveable(perm_state))

        perm_state = [3, 9, 1, 15, 14, 11, 4, 6, 13, 16, 10, 12, 2, 7, 8, 5]
        self.assertFalse(solveable(perm_state))

if __name__ == '__main__':
    unittest.main()
