import unittest
from pyraminx import *

class TestPyraminx(unittest.TestCase):
    def test_perm_inverse(self):
        start = init_pyraminx()
        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[INV_RIGHT], PERMS[RIGHT]))
        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[RIGHT], PERMS[INV_RIGHT]))

        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[INV_LEFT], PERMS[LEFT]))
        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[LEFT], PERMS[INV_LEFT]))

        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[INV_TOP], PERMS[TOP]))
        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[TOP], PERMS[INV_TOP]))

        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[BACK], PERMS[INV_BACK]))
        self.assertEqual(start.perm,
                         px_perm_mul(PERMS[INV_BACK], PERMS[BACK]))

    def test_cyc_add(self):
        c1 = (0, 1, 1, 1, 1, 0)
        c2 = (0, 1, 1, 0, 1, 1)
        self.assertEqual(px_cyc_add(c1, c1), (0,0,0,0,0,0))
        self.assertEqual(px_cyc_add(c1, c2), (0,0,0,1,0,1))

    def test_wreath_inverse(self):
        start = init_pyraminx()
        self.assertEqual(start, inv_top(top(start)))
        self.assertEqual(start, inv_back(back(start)))
        self.assertEqual(start, inv_right(right(start)))
        self.assertEqual(start, inv_left(left(start)))

    def test_move_three_cycle(self):
        start = init_pyraminx()
        face_moves = [top, back, right, left, inv_top, inv_back, inv_right, inv_left]
        for move in face_moves:
            puzz = move(start)
            puzz = move(puzz)
            puzz = move(puzz)

            self.assertEqual(start, puzz)

if __name__ == '__main__':
    unittest.main()
