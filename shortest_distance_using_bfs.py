import math

def shortest_distance(graph, start, end):
    visited = {}
    prev = {}

    q = [(start, 0)]
    visited.update({ start: None })
    prev.update({ start: None })

    while len(q) > 0:
        current, dist = q.pop()
        if current == end:
            return dist, build_path(prev, current)
        for neigh in graph[current]:
            if not neigh in visited:
                q.insert(0, (neigh, dist+1))
                visited.update({ neigh: None })
                prev.update({ neigh: current })

    return math.inf, []

def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def build_path(prev, current):
    path = [current]

    while not prev[current] is None:
        path.insert(0, prev[current])
        current = prev[current]

    return path

if __name__ == '__main__':
    """
        Consider the graph:
            a -- b -- e -- g
            |    |         |
            c -- d -- f -- +
        Find the shortest distance from g to c 
    """
    edges = [
        ('a', 'b'),
        ('b', 'e'),
        ('a', 'c'),
        ('b', 'd'),
        ('c', 'd'),
        ('d', 'f'),
        ('e', 'g'),
        ('f', 'g'),
    ]
    graph = build_graph(edges)
    begin, end = 'g', 'c'
    dist, path = shortest_distance(graph, begin, end)
    print('Shortest distance between {} and {}: {}'.format(
        begin, end, dist
    ))
    print('Shortest path from {} to {}: {}'.format(
        begin, end, path
    ))
