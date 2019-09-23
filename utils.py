def n_inversions(perm):
    n_invs = 0
    for idx, x in enumerate(perm):
        for ridx in range(idx+1, len(perm)):
            if x > perm[ridx]:
                n_invs += 1

    return n_invs


def even_perm(perm):
    return ((n_inversions(perm) % 2) == 0)

def solveable(perm_state):
    '''
    Params:
        perm_state: list of ints, where the element {len(perm_state)}
                    denotes the empty tile
    Returns:
        True/False
    '''
    n = int(len(perm_state) ** 0.5)
    idx = perm_state.index(len(perm_state))
    perm = [i for i in perm_state if i != len(perm_state)]

    empty_x = idx // n
    if n % 2 == 1:
        return even_perm(perm)
    else:
        nth_from_bot = n - empty_x
        return ((n_inversions(perm) % 2 == 1) and (nth_from_bot % 2 == 0)) or \
               ((n_inversions(perm) % 2 == 0) and (nth_from_bot % 2 == 1))
