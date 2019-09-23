import unittest
from puzzle import TileNode

class TestPuzzle(unittest.TestCase):
    def test_moves_3(self):
        state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        up = [1, 2, 3, 4, 5, 9, 7, 8, 6]
        left = [1, 2, 3, 4, 5, 6, 7, 9, 8]

        puzzle = TileNode(state)
        node_up = puzzle.move_up()
        node_down = puzzle.move_down()
        node_left = puzzle.move_left()
        node_right = puzzle.move_right()

        self.assertListEqual(node_up.state, up)
        self.assertEqual(node_down, None)
        self.assertListEqual(node_left.state, left)
        self.assertEqual(node_right, None)

    def test_moves_mid(self):
        state = [1, 3, 4, 8, 9, 7, 2, 6, 5]
        up    = [1, 9, 4, 8, 3, 7, 2, 6, 5]
        down  = [1, 3, 4, 8, 6, 7, 2, 9, 5]
        left  = [1, 3, 4, 9, 8, 7, 2, 6, 5]
        right = [1, 3, 4, 8, 7, 9, 2, 6, 5]

        puzzle = TileNode(state)
        node_up = puzzle.move_up()
        node_down = puzzle.move_down()
        node_left = puzzle.move_left()
        node_right = puzzle.move_right()

        self.assertListEqual(node_up.state, up)
        self.assertListEqual(node_down.state, down)
        self.assertListEqual(node_left.state, left)
        self.assertListEqual(node_right.state, right)

    def test_moves_4(self):
        state = [16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]
        down  = [5, 2, 3, 4, 16, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]
        right = [2, 16, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]

        puzzle = TileNode(state)
        node_up = puzzle.move_up()
        node_down = puzzle.move_down()
        node_left = puzzle.move_left()
        node_right = puzzle.move_right()

        self.assertEqual(node_up, None)
        self.assertListEqual(node_down.state, down)
        self.assertEqual(node_left, None)
        self.assertListEqual(node_right.state, right)

    def test_moves_mid_4(self):
        state = [1, 3, 4, 8, 9, 7, 2, 6, 5, 16, 11, 12, 13, 14, 15, 10]
        up    = [1, 3, 4, 8, 9, 16, 2, 6, 5, 7, 11, 12, 13, 14, 15, 10]
        down  = [1, 3, 4, 8, 9, 7, 2, 6, 5, 14, 11, 12, 13, 16, 15, 10]
        left  = [1, 3, 4, 8, 9, 7, 2, 6, 16, 5, 11, 12, 13, 14, 15, 10]
        right = [1, 3, 4, 8, 9, 7, 2, 6, 5, 11, 16, 12, 13, 14, 15, 10]

        puzzle = TileNode(state)
        node_up = puzzle.move_up()
        node_down = puzzle.move_down()
        node_left = puzzle.move_left()
        node_right = puzzle.move_right()

    def test_moves(self):
        puzzle = TileNode([1, 2, 3, 4])
        p = puzzle.move_up()
        self.assertEqual(p.distance, 1)
        p = p.move_left()
        self.assertEqual(p.distance, 2)
        p = p.move_down()
        self.assertEqual(p.distance, 3)
        self.assertListEqual(p.get_moves(), ['U', 'L', 'D'])

        p = p.move('U')
        p = p.move('R')
        p = p.move('D')
        self.assertEqual(p.distance, 6) # eh ...
        self.assertListEqual(p.get_moves(), ['U', 'L', 'D', 'U', 'R', 'D'])

if __name__ == '__main__':
    unittest.main()
