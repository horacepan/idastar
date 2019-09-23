from queue import PriorityQueue
import pdb
import time
import numpy as np
from heuristics import manhattan
from puzzle import *
from utils import check_memory

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
    node = TileNode([6, 8, 5, 1, 9, 7, 4, 2, 3]) # expect 24
    print(node)
    print('Running A* search ...')
    results = astar(node, manhattan)
    print(results)
    print('Expected distance: 24')
    check_memory()
