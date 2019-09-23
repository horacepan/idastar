import pdb
import random
from utils import even_perm, n_inversions, solveable

def gen_new_state(state, old_idx, new_idx):
    '''
    Returns a new state with the elements at the indices swapped
    Params:
        state: list of ints of tile puzzle state
        old_idx: int index of item to be swapped
        new_idx: other index to be swapped
    Returns:
        list of ints
    '''
    new_state = state[:]
    new_state[old_idx], new_state[new_idx] = new_state[new_idx], new_state[old_idx]
    return new_state

class TileNode(object):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    MOVE_MAP = ['U', 'R', 'D', 'L']

    def __init__(self, state, prev_node=None, last_move=None, idx=None):
        self.state = state
        self.prev_node = prev_node
        self.last_move = last_move
        self.size = int(len(state) ** 0.5)
        self.idx = self.state.index(len(self.state))
        self.distance = 0 if prev_node is None else prev_node.distance + 1

        if idx is None:
            self.idx = self.state.index(len(state))

    def __repr__(self):
        str_rep = ''
        i = 0
        for i in range(self.size):
            lst = self.state[i * self.size: i * self.size + self.size]
            str_rep += (('[{:2d}]' * self.size).format(*lst) + '\n')
            i += self.size
        return str_rep

    def is_solved(self):
        return all([v == idx + 1 for idx, v in enumerate(self.state)])

    def expand(self):
        '''

        '''
        nbrs = [
            self.move_up(), self.move_down(), self.move_right(), self.move_left()
        ]
        return [x for x in nbrs if x is not None]

    def move_up(self):
        new_idx = self.idx - self.size
        if new_idx < 0:
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.UP, new_idx)

    def move_down(self):
        new_idx = self.idx + self.size
        if new_idx > len(self.state):
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.DOWN, new_idx)

    def move_right(self):
        new_idx = self.idx + 1
        if (new_idx % self.size) == 0:
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.RIGHT, new_idx)

    def move_left(self):
        new_idx = self.idx - 1
        if (new_idx % self.size) == (self.size - 1):
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.LEFT, new_idx)

    @staticmethod
    def random(size):
        state = [i for i in range(1, size * size + 1)]
        random.shuffle(state)

        while not solveable(state):
            random.shuffle(state)

        return TileNode(state)

    def get_moves(self):
        if self.prev_node is None:
            return []
        return self.prev_node.get_moves() + [TileNode.MOVE_MAP[self.last_move]]

if __name__ == '__main__':
    puzzle = TileNode.random(3)
    print(puzzle)
