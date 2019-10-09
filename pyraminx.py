import pdb
from collections import namedtuple
import random

######################
# Pyraminx constants #
######################
RIGHT = 0
LEFT = 1
TOP = 2
BACK = 3
INV_RIGHT = 4
INV_LEFT = 5
INV_TOP = 6
INV_BACK = 7
FACES = [RIGHT, LEFT, TOP, BACK, INV_RIGHT, INV_LEFT, INV_TOP, INV_BACK]

ORIENTATIONS = {
    RIGHT: (0, 0, 1, 1, 0, 0),
    LEFT:  (1, 1, 0, 0, 0, 0),
    TOP:   (1, 0, 1, 0, 0, 0),
    BACK:  (0, 0, 0, 1, 1, 0),
    INV_RIGHT: (0, 1, 1, 0, 0, 0),
    INV_LEFT:  (1, 0, 0, 0, 0, 1),
    INV_TOP:   (0, 0, 1, 0, 1, 0),
    INV_BACK:  (0, 0, 0, 1, 0, 1),
}

PERMS = {
    RIGHT: (1, 3, 4, 2, 5, 6),
    LEFT:  (2, 6, 3, 4, 5, 1),
    TOP:   (5, 2, 1, 4, 3, 6),
    BACK:  (1, 2, 3, 5, 6, 4),
    INV_RIGHT: (1, 4, 2, 3, 5, 6),
    INV_LEFT:  (6, 1, 3, 4, 5, 2),
    INV_TOP:   (3, 2, 5, 4, 1, 6),
    INV_BACK:  (1, 2, 3, 6, 4, 5)
}

TIPS = {
    RIGHT: (1, 0, 0, 0),
    LEFT:  (0, 1, 0, 0),
    TOP:   (0, 0, 1, 0),
    BACK:  (0, 0, 0, 1),
    INV_RIGHT: (2, 0, 0, 0),
    INV_LEFT:  (0, 2, 0, 0),
    INV_TOP:   (0, 0, 2, 0),
    INV_BACK:  (0, 0, 0, 2)
}

###################################
# Pyraminx algebra util functions #
###################################

def px_perm_mul(p1, p2):
    '''
    apply p1 to p2
    '''
    return (
        p1[p2[0] - 1],
        p1[p2[1] - 1],
        p1[p2[2] - 1],
        p1[p2[3] - 1],
        p1[p2[4] - 1],
        p1[p2[5] - 1],
    )

def px_perm_dot(perm, tup):
    pinv = px_perm_inv(perm)
    return (
        tup[pinv[0]-1],
        tup[pinv[1]-1],
        tup[pinv[2]-1],
        tup[pinv[3]-1],
        tup[pinv[4]-1],
        tup[pinv[5]-1]
    )

# indexing is actually faster than doing a dic
def px_perm_inv(perm):
    return (perm.index(1) + 1,
            perm.index(2) + 1,
            perm.index(3) + 1,
            perm.index(4) + 1,
            perm.index(5) + 1,
            perm.index(6) + 1)

def px_cyc_add(c1, c2, n):
    return tuple(
        (c1[i] + c2[i]) % n for i in range(len(c1))
    )

Pyraminx = namedtuple('Pyraminx', ['orientation', 'perm'])
PyrTip = namedtuple('PyrTip', ['orientation', 'perm', 'tip'])

def px_wreath_mul(c1, p1, c2, p2):
    p1_dot_c2 = px_perm_dot(p1, c2)
    ori = px_cyc_add(c1, p1_dot_c2, 2)
    perm = px_perm_mul(p1, p2)
    return ori, perm

def px_inv(c, p):
    pinv = px_perm_inv(p)
    invc = tuple((2 - i) % 2 for i in c)
    cinv = px_perm_dot(pinv, invc)
    return cinv, pinv

#############################
# Pyraminx puzzle functions #
#############################

def init_pyraminx():
    return Pyraminx((0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6))

def init_pyraminx_tip():
    return PyrTip((0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6), (0, 0, 0, 0))

def move_face_tip(puzzle, face):
    face_ori = ORIENTATIONS[face]
    face_perm = PERMS[face]
    face_tip = TIPS[face]
    tip = px_cyc_add(face_tip, puzzle.tip, 3)
    ori, perm = px_wreath_mul(face_ori, face_perm,
                              puzzle.orientation, puzzle.perm)
    return PyrTip(ori, perm, tip)

def move_face(puzzle, face):
    face_ori = ORIENTATIONS[face]
    face_perm = PERMS[face]
    ori, perm = px_wreath_mul(face_ori, face_perm,
                              puzzle.orientation, puzzle.perm)
    return Pyraminx(ori, perm)

def top(puzzle):
    return move_face(puzzle, TOP)

def back(puzzle):
    return move_face(puzzle, BACK)

def right(puzzle):
    return move_face(puzzle, RIGHT)

def left(puzzle):
    return move_face(puzzle, LEFT)

def inv_top(puzzle):
    return move_face(puzzle, INV_TOP)

def inv_back(puzzle):
    return move_face(puzzle, INV_BACK)

def inv_right(puzzle):
    return move_face(puzzle, INV_RIGHT)

def inv_left(puzzle):
    return move_face(puzzle, INV_LEFT)

def move_tip(puzzle, face):
    tip = px_cyc_add(TIPS[face], puzzle.tip, 3)
    return PyrTip(puzzle.orientation, puzzle.perm, tip)

def rtip(puzzle):
    return move_tip(puzzle, RIGHT)

def ltip(puzzle):
    return move_tip(puzzle, LEFT)

def ttip(puzzle):
    return move_tip(puzzle, TOP)

def btip(puzzle):
    return move_tip(puzzle, BACK)

def irtip(puzzle):
    return move_tip(puzzle, INV_RIGHT)

def iltip(puzzle):
    return move_tip(puzzle, INV_LEFT)

def ittip(puzzle):
    return move_tip(puzzle, INV_TOP)

def ibtip(puzzle):
    return move_tip(puzzle, INV_BACK)

def pyraminx_nbrs(puzzle):
    nbrs = [
        top(puzzle),
        back(puzzle),
        right(puzzle),
        left(puzzle),
        inv_top(puzzle),
        inv_back(puzzle),
        inv_right(puzzle),
        inv_left(puzzle),
    ]
    return nbrs

def pyraminx_tip_nbrs(puzzle):
    nbrs = [
        top(puzzle),
        back(puzzle),
        right(puzzle),
        left(puzzle),
        inv_top(puzzle),
        inv_back(puzzle),
        inv_right(puzzle),
        inv_left(puzzle),
        rtip(puzzle),
        ltip(puzzle),
        ttip(puzzle),
        btip(puzzle),
        irtip(puzzle),
        iltip(puzzle),
        ittip(puzzle),
        ibtip(puzzle),

    ]
    return nbrs

def random_state():
    puzzle = init_pyraminx()
    for _ in range(100):
        puzzle = random.choice(pyraminx_nbrs(puzzle))

    return puzzle

def str_unpack(tup):
    return ('{}' * len(tup)).format(*tup)

def pyraminx_str(puzzle):
    ori, perm = puzzle
    str_rep = '{},{}'.format(str_unpack(ori), str_unpack(perm))
    return str_rep

def pyraminx_tip_str(puzzle):
    ori, perm, tip = puzzle
    str_rep = '{},{},{}'.format(str_unpack(ori), str_unpack(perm), str_unpack(tip))
    return str_rep

if __name__ == '__main__':
    test()
