"""
    Number of ways to traverse an n x m
    starting from upper left corner to lower right corner
    either by moving down or moving right one cell
    at a time.
"""
def traverse_grid(n, m, memo={}):
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    curr_loc = '{},{}'.format(n, m)
    if curr_loc in memo:
        return memo[curr_loc]
    memo[curr_loc] = traverse_grid(n - 1, m) + traverse_grid(n, m - 1)
    return memo[curr_loc]

if __name__ == '__main__':
    grids = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 5),
        (10, 10),
        (10, 25),
    ]
    for (n, m) in grids:
        print('{} ways to traverse grid of size {} x {}'.format(
            traverse_grid(n, m), n, m
        ))
