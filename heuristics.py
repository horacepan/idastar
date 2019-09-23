def manhattan(state):
    '''
    Params:
        state: list of ints
    '''
    cnt = 0
    for idx, val in enumerate(state):
        cnt += (1 if val != (idx + 1) else 0)
    return cnt

def test_dist():
    perm = [1, 4, 2, 3]
    print(manhattan(perm))

if __name__ == '__main__':
    test_dist()
