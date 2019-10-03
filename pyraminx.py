from collections import namedtuple

####################
# Pyraminx constants
####################
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
    RIGHT: (0, 1, 1, 0, 0, 0),
    LEFT:  (1, 0, 0, 0, 0, 1),
    TOP:   (0, 0, 1, 0, 1, 0),
    BACK:  (0, 0, 0, 1, 0, 1),
    INV_RIGHT: (0, 0, 1, 1, 0, 0),
    INV_LEFT:  (1, 1, 0, 0, 0, 0),
    INV_TOP:   (1, 0, 1, 0, 0, 0),
    INV_BACK:  (0, 0, 0, 1, 1, 0),
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

def px_cyc_add(c1, c2):
    return (
        (c1[0] + c2[0]) % 2,
        (c1[1] + c2[1]) % 2,
        (c1[2] + c2[2]) % 2,
        (c1[3] + c2[3]) % 2,
        (c1[4] + c2[4]) % 2,
        (c1[5] + c2[5]) % 2
    )

Pyraminx = namedtuple('Pyraminx', ['orientation', 'perm'])
def px_wreath_mul(c1, p1, c2, p2):
    p1_dot_c2 = px_perm_dot(p1, c2)
    ori = px_cyc_add(c1, p1_dot_c2)
    perm = px_perm_mul(p1, p2)
    return ori, perm

#############################
# Pyraminx puzzle functions #
#############################

def init_pyraminx():
    return Pyraminx((0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6))

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

def test():
    start = init_pyraminx()
    face_moves = [top, back, right, left, inv_top, inv_back, inv_right, inv_left]
    start = init_pyraminx()
    for move in face_moves:
        puzz = move(start)
        puzz = move(puzz)
        puzz = move(puzz)
        print(puzz, move)

    print('test inverses')
    print('t, t inv: {}'.format(inv_top(top(start))))
    print('b, b inv: {}'.format(inv_back(back(start))))
    print('r, r inv: {}'.format(inv_right(right(start))))
    print('l, l inv: {}'.format(inv_left(left(start))))

if __name__ == '__main__':
    test()
