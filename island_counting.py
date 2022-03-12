"""
    Given a two dimensional array where
        L denotes land and where lands that are adjacent
          horizontally and vertically belong to the same island
        W denotes water
            w w L w w w L w w
            w L L w w w L W W
            W L W W L W L L W
            W W L W L L W L W
            W W L W L W W W L
            W W W W W L L W L
            W W W W W W W L L
            L L W W L L W W W
            W W W W W W W W W
            W L W W L W L W L
        Count the number of islands in the array
"""
def count_islands(frontier):
    n_islands = 0
    explored = {}

    for i in range(len(frontier)):
        for j in range(len(frontier[i])):
            if frontier[i][j] == 'W':
                continue
            if explore(frontier, i, j, explored) == True:
                n_islands += 1

    return n_islands

def get_frontier1():
    return [
        ['L', 'W'],
        ['W', 'W']
    ]

def get_frontier2():
    return [
        ['L','W'],
        ['W','L']
    ]

def get_frontier3():
    return [
        ['L','L','W','W'],
        ['W','W','W','W'],
        ['W','L','W','L'],
        ['W','W','L','L'],
    ]

def get_frontier4():
    return [
        ['L','L','W','W','L'],
        ['W','W','W','W','L'],
        ['W','W','W','W','W'],
        ['L','W','W','L','L'],
        ['L','L','W','L','L'],
    ]

def get_frontier5():
    return [
        ['L','L','W','W','L'],
        ['W','W','W','W','L'],
        ['W','W','L','W','W'],
        ['L','W','W','L','L'],
        ['L','L','W','L','L'],
    ]

def get_big_frontier():
    return [
        ['W','W','L','W','W','W','L','W','W'],
        ['W','L','L','W','W','W','L','W','W'],
        ['W','L','W','W','L','W','L','L','W'],
        ['W','W','L','W','L','L','W','L','W'],
        ['W','W','L','W','L','W','W','W','L'],
        ['W','W','W','W','W','L','L','W','L'],
        ['W','W','W','W','W','W','W','L','L'],
        ['L','L','W','W','L','L','W','W','W'],
        ['W','W','W','W','W','W','W','W','W'],
        ['W','L','W','W','L','W','L','W','L'],
    ]

def explore(frontier, i, j, explored):
    i_inbounds = 0 <= i and i < len(frontier)
    j_inbounds = 0 <= j and j < len(frontier[0])

    if not i_inbounds or not j_inbounds:
        return False

    if frontier[i][j] == 'W':
        return False

    this_land = '{},{}'.format(i, j)
    if this_land in explored:
        return False

    explored.update({ this_land: None })
    explore(frontier, i-1, j, explored)
    explore(frontier, i+1, j, explored)
    explore(frontier, i, j-1, explored)
    explore(frontier, i, j+1, explored)

    return True

if __name__ == '__main__':
    frontiers = [
        get_frontier1,
        get_frontier2,
        get_frontier3,
        get_frontier4,
        get_frontier5,
        get_big_frontier,
    ]

    for i in range(len(frontiers)):
        print('Number of islands: {}'.format(
            count_islands(frontiers[i]())
        ))
