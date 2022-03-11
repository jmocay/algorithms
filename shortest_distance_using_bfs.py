import math

def shortest_distance(graph, start, end):
    visited = {}
    q = [(start, 0)]
    visited.update({ start: None })
    while len(q) > 0:
        current, dist = q.pop()
        if current == end:
            return dist
        for neigh in graph[current]:
            if not neigh in visited:
                q.insert(0, (neigh, dist+1))
                visited.update({ neigh: None })
    return math.inf

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

if __name__ == '__main__':
    """
        Consider the graph:
            a -- b -- e -- g
            |    |         |
            c -- d -- f -- +
        Find the shortest distance from a to g 
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
    print('Shortest distance between {} and {}: {}'.format(
        'a', 'g',
        shortest_distance(graph, 'a', 'g')
    ))
