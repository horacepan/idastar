import time
import sys
from queue import deque
from pyraminx import pyraminx_nbrs, init_pyraminx, pyraminx_str, Pyraminx, init_pyraminx_tip, pyraminx_tip_str, pyraminx_tip_nbrs
from utils import check_memory

'''
neighbors
pyraminx_fmt
'''
def bfs(fname):
    #start = init_pyraminx()
    start = init_pyraminx_tip()
    to_visit = deque([(start, 0)])
    visited = set()

    with open(fname, 'w') as f:
        while to_visit:
            curr, dist = to_visit.popleft()
            if curr in visited:
                continue

            #f.write('{},{}\n'.format(pyraminx_str(curr), dist))
            f.write('{},{}\n'.format(pyraminx_tip_str(curr), dist))
            visited.add(curr)
            for nbr in pyraminx_tip_nbrs(curr):
                if nbr not in visited:
                    to_visit.append((nbr, dist + 1))
    check_memory()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = 'dists_tips.txt'
    print('Saving in: {}'.format(fname))
    start = time.time()
    bfs(fname)
    print('Elapsed: {:.2f}s'.format(time.time() - start))
