from pyraminx import  px_wreath_mul, str_unpack

CUBE2_IDENT = ((0,) * 8, tuple(range(1, 9)))
CUBE3_IDENT = ((0,) * 8, tuple(range(1, 9)), (0,) * 12, tuple(range(1, 13)))

CUBE2_GENERATORS = [
    ((0, 0, 0, 0, 0, 0, 0, 0), (4, 2, 3, 5, 8, 6, 7, 1)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (8, 2, 3, 1, 4, 6, 7, 5)),
    ((2, 1, 0, 0, 0, 0, 2, 1), (2, 7, 3, 4, 5, 6, 8, 1)),
    ((2, 1, 0, 0, 0, 0, 2, 1), (8, 1, 3, 4, 5, 6, 2, 7)),
    ((1, 2, 1, 2, 0, 0, 0, 0), (2, 3, 4, 1, 5, 6, 7, 8)),
    ((1, 2, 1, 2, 0, 0, 0, 0), (4, 1, 2, 3, 5, 6, 7, 8))
]

CUBE2_DOUBLE_GENERATORS = [
    ((0, 0, 0, 0, 0, 0, 0, 0), (5, 2, 3, 8, 1, 6, 7, 4)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (5, 2, 3, 8, 1, 6, 7, 4)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (7, 8, 3, 4, 5, 6, 1, 2)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (7, 8, 3, 4, 5, 6, 1, 2)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (3, 4, 1, 2, 5, 6, 7, 8)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (3, 4, 1, 2, 5, 6, 7, 8))
]

CUBE2_KGROUP_GENERATORS = [
    ((0, 0, 0, 0, 0, 0, 0, 0), (4, 2, 3, 5, 8, 6, 7, 1)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 3, 6, 4, 5, 7, 2, 8)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (7, 8, 3, 4, 5, 6, 1, 2)),
    ((2, 1, 2, 1, 2, 1, 2, 1), (2, 7, 4, 5, 6, 3, 8, 1)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (3, 4, 1, 2, 5, 6, 7, 8)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 7, 8, 5, 6))
]

CUBE3_GENS = [
    ((0, 0, 0, 0, 0, 0, 0, 0), (2, 3, 4, 1, 5, 6, 7, 8), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (2, 3, 4, 1, 5, 6, 7, 8, 9, 10, 11, 12)),
    ((0, 0, 1, 2, 0, 0, 2, 1), (1, 2, 7, 3, 5, 6, 8, 4), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 7, 4, 5, 6, 11, 3, 9, 10, 8, 12)),
    ((2, 0, 0, 1, 1, 0, 0, 2), (4, 2, 3, 8, 1, 6, 7, 5), (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1), (1, 2, 3, 8, 4, 6, 7, 12, 9, 10, 11, 5)),
    ((0, 1, 2, 0, 0, 2, 1, 0), (1, 6, 2, 4, 5, 7, 3, 8), (0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0), (1, 6, 3, 4, 5, 10, 2, 8, 9, 7, 11, 12)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 8, 5, 6, 7), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6, 7, 8, 12, 9, 10, 11)),
    ((1, 2, 0, 0, 2, 1, 0, 0), (5, 1, 3, 4, 6, 2, 7, 8), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (5, 2, 3, 4, 9, 1, 7, 8, 6, 10, 11, 12)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (4, 1, 2, 3, 5, 6, 7, 8), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (4, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12)),
    ((0, 0, 1, 2, 0, 0, 2, 1), (1, 2, 4, 8, 5, 6, 3, 7), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 8, 4, 5, 6, 3, 11, 9, 10, 7, 12)),
    ((2, 0, 0, 1, 1, 0, 0, 2), (5, 2, 3, 1, 8, 6, 7, 4), (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1), (1, 2, 3, 5, 12, 6, 7, 4, 9, 10, 11, 8)),
    ((0, 1, 2, 0, 0, 2, 1, 0), (1, 3, 7, 4, 5, 2, 6, 8), (0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0), (1, 7, 3, 4, 5, 2, 10, 8, 9, 6, 11, 12)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 6, 7, 8, 5), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 9)),
    ((1, 2, 0, 0, 2, 1, 0, 0), (2, 6, 3, 4, 1, 5, 7, 8), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (6, 2, 3, 4, 1, 9, 7, 8, 5, 10, 11, 12)),
]

CUBE2_CHECK = [
    ((0, 0, 0, 0, 0, 0, 0, 0), (2, 3, 4, 1, 5, 6, 7, 8)),
    ((0, 0, 1, 2, 0, 0, 2, 1), (1, 2, 7, 3, 5, 6, 8, 4)),
    ((2, 0, 0, 1, 1, 0, 0, 2), (4, 2, 3, 8, 1, 6, 7, 5)),
    ((0, 1, 2, 0, 0, 2, 1, 0), (1, 6, 2, 4, 5, 7, 3, 8)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 8, 5, 6, 7)),
    ((1, 2, 0, 0, 2, 1, 0, 0), (5, 1, 3, 4, 6, 2, 7, 8)),

    ((0, 0, 0, 0, 0, 0, 0, 0), (4, 1, 2, 3, 5, 6, 7, 8)),
    ((0, 0, 1, 2, 0, 0, 2, 1), (1, 2, 4, 8, 5, 6, 3, 7)),
    ((2, 0, 0, 1, 1, 0, 0, 2), (5, 2, 3, 1, 8, 6, 7, 4)),
    ((0, 1, 2, 0, 0, 2, 1, 0), (1, 3, 7, 4, 5, 2, 6, 8)),
    ((0, 0, 0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 6, 7, 8, 5)),
    ((1, 2, 0, 0, 2, 1, 0, 0), (2, 6, 3, 4, 1, 5, 7, 8)),
]

def init_2cube():
    return CUBE2_IDENT

def init_3cube():
    return CUBE3_IDENT

def cube2_nbrs(s):
    so, sp = s
    return [px_wreath_mul(no, np, so, sp, 3) for (no, np) in CUBE2_GENERATORS]

def cube3_nbrs(s):
    ct, cp, et, ep = s
    return [(*px_wreath_mul(nct, ncp, ct, cp, 3), *px_wreath_mul(net, nep, et, ep, 2)) for (nct, ncp, net, nep) in CUBE3_GENS]

def cube2_check(s):
    so, sp = s
    return [px_wreath_mul(no, np, so, sp, 3) for (no, np) in CUBE2_CHECK]

def cube2_check_small(s):
    so, sp = s
    return [px_wreath_mul(no, np, so, sp, 3) for (no, np) in CUBE2_CHECK[:6]]

def cube2_double_nbrs(s):
    so, sp = s
    return [px_wreath_mul(no, np, so, sp, 3) for (no, np) in CUBE2_DOUBLE_GENERATORS]

def cube2_group_nbrs(s):
    so, sp = s
    return [px_wreath_mul(no, np, so, sp, 3) for (no, np) in CUBE2_KGROUP_GENERATORS]

def cube2_fmt(g):
    ori, perm = g
    str_rep = '{},{}'.format(str_unpack(ori), str_unpack(perm))
    return str_rep

def cube3_fmt(g):
    ct, cp, et, ep = g
    str_rep = '{},{},{},{}'.format(
        str_unpack(ct), 
        str_unpack(ct), 
        str_unpack(ct), 
        str_unpack(ct)
    )
    return str_rep

def double_moves():
    for m in CUBE2_GENERATORS:
        print(px_wreath_mul(m[0], m[1], m[0], m[1], 3))
