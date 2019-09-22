def gen_new_state(state, old_idx, new_idx):
    new_state = state[:]
    new_state[old_idx], new_state[new_idx] = new_state[new_idx], new_state[old_idx]
    return new_state

class TileNode(object):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, state, prev_node=None, last_move=None, idx=None):
        self.state = state
        self.prev_node = prev_node
        self.last_move = last_move
        self.size = int(len(state) ** 0.5)
        self.idx = self.state.index(len(self.state))

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

    def get_moves(self):
        cnt = 0
        curr = self

        while curr is not None:
            curr = curr.prev_node
            cnt += 1
        return cnt

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
        return TileNode(new_state, self, TileNode.UP, new_idx)

    def move_right(self):
        new_idx = self.idx + 1
        if (new_idx % self.size) == 0:
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.UP, new_idx)

    def move_left(self):
        new_idx = self.idx - 1
        if (new_idx % self.size) == (self.size - 1):
            return None

        new_state = gen_new_state(self.state, self.idx, new_idx)
        return TileNode(new_state, self, TileNode.UP, new_idx)

if __name__ == '__main__':
    state = [1, 3, 4, 8, 9, 7, 2, 6, 5, 16, 11, 12, 13, 14, 15, 10]
    puzzle = TileNode(state)
    print(puzzle)