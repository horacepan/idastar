import time
import numpy as np
from heuristics import *
from puzzle import *
from utils import check_memory

def idastar(node, heuristic, global_max):
    start = time.time()

    nodes_explored = 0
    results = {'nodes_explored': 0}
    max_depth = heuristic(node.state)
    while (max_depth <= global_max):
        # search the graph up to this given max depth
        t = idastar_node(node, 0, max_depth, heuristic, results)

        # search will generally return a number, and a list of states if correct
        if not isinstance(t, int):
            # found solution!
            results['distance'] = t.distance
            results['moves'] = t.get_moves()
            break

        max_depth += 1
    results['time'] = time.time() - start
    return results

def idastar_node(node, depth, max_depth, heuristic, results):
    h = heuristic(node.state)
    if (h + depth > max_depth):
        return h

    if node.is_solved():
        return node

    results['nodes_explored'] += 1
    for s in node.expand():
        t = idastar_node(s, depth + 1, max_depth, heuristic, results)
        if not isinstance(t, int):
            # not returning an int == solved
            return t

        if (t - 1 > h):
            h = t - 1
            # dont understand why we do this
            if depth + h > max_depth:
                return h
    return h

if __name__ == '__main__':
    #node = TileNode([7, 4, 5, 1, 9, 6, 2, 3, 8])
    #node = TileNode([8, 1, 5, 4, 2, 3, 6, 9, 7])
    node = TileNode([6, 8, 5, 1, 9, 7, 4, 2, 3]) # expect 24
    print(node)
    print('Running IDA* search ...')
    results = idastar(node, manhattan, 31)
    print(results)
    print('Expected distance: 21')
    check_memory()
