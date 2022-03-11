"""
  Breadth First Search
    graph = dict of node to list of adjacent vertices
    s = starting node
    f = function to process a node
    visited = dictionary to track visited vertices
"""
def bfs(graph, s, f, visited):
    q = [s]
    while len(q) > 0:
        current = q.pop()
        if current in visited:
            continue
        visited.update({current: None})
        f(current)
        for neigh in graph[current]:
            if not neigh in visited:
                q.insert(0, neigh)

def build_graph():
    """
      A -- C 
      |    |
      B -- E -- G
      |
      D -- F
    """
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B', 'F'],
        'E': ['B', 'G'],
        'F': ['D'],
        'G': ['E']
    }

def process_node(node):
    print(node)

if __name__ == '__main__':
    graph = build_graph()
    visited = {}
    bfs(graph, 'A', process_node, visited)
