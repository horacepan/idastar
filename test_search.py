import unittest
from puzzle import TileNode
from astar import *
from idastar import *
from heuristics import manhattan
from utils import to_string

class TestAstar(unittest.TestCase):
    def test_search_manhattan(self):
        puzzle = TileNode([7, 4, 5, 1, 9, 6, 2, 3, 8])
        results = astar(puzzle, manhattan)
        #results = idastar(puzzle, manhattan, 31)
        moves = results['moves']

        for m in results['moves']:
            puzzle = puzzle.move(m)

        self.assertEqual(len(results['moves']), results['distance'])
        self.assertTrue(puzzle.is_solved())

if __name__ == '__main__':
    unittest.main()
