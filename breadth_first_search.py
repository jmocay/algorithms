"""
  Breadth First Search
    graph = dict of node to list of adjacent nodes
    s = starting node
    f = function to process a node
"""
def bfs(graph, s, f):
    q = [s]
    while len(q) > 0:
        current = q.pop()
        f(current)
        for neigh in graph[current]:
            q.insert(0, neigh)

def build_graph():
    """
      A -- C 
      |    |
      B    E
      |
      D -- F
    """
    return {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['F'],
        'E': [],
        'F': [] 
    }

def process_node(node):
    print(node)

if __name__ == '__main__':
    graph = build_graph()
    bfs(graph, 'A', process_node)
