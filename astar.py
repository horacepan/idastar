from queue import PriorityQueue
import pdb
import time
import numpy as np
from heuristics import manhattan
from puzzle import *

def astar(node, heuristic):
    results = {}
    nodes_explored = 0
    distance = None
    moves = []

    # =========== A* search  ============ #
    start = time.time()
    curr_node = node
    to_visit = PriorityQueue()
    to_visit.put((heuristic(node.state), node))
    while not to_visit.empty():
        val, curr_node = to_visit.get()
        nodes_explored += 1

        if curr_node.is_solved():
            results['moves'] = curr_node.get_moves()
            results['distance'] = curr_node.distance
            break

        for n in curr_node.expand():
            fitness = n.distance + heuristic(n.state)
            to_visit.put((fitness, n))

    # =========== algorithm end ============ #

    results['nodes_explored'] = nodes_explored
    results['time'] = time.time() - start
    return results
'''
expect node object to have the functions:
- is_solved: True/False
- get_moves: int
- expand: neighbors
'''

if __name__ == '__main__':
    node = TileNode([2, 8, 3, 1, 5, 6, 4, 7, 9])
    node = TileNode([9, 3, 6, 1, 2, 7, 4, 5, 8])
    print(node)
    print('Running A* search ...')
    results = astar(node, manhattan)
    print(results)
