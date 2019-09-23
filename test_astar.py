import unittest
from puzzle import TileNode
from astar import *
from heuristics import manhattan
from utils import to_string

class TestAstar(unittest.TestCase):
    def test_astar_manhattan(self):
        n = 10
        for i in range(n):
            puzzle = TileNode.random(3)
            print(to_string(puzzle.state))
            results = astar(puzzle, manhattan)
            moves = results['moves']

            for m in results['moves']:
                puzzle = puzzle.move(m)

            self.assertEqual(len(results['moves']), results['distance'])
            self.assertTrue(puzzle.is_solved())
            print('Found solution to {} of {}: {}'.format(i + 1, n, results))

if __name__ == '__main__':
    unittest.main()
