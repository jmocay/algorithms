"""
  Depth First Search
    graph = dict of node to list of adjacent nodes
    s = starting node
    f = function to process a node
    visited = dictionary to track visited vertices
"""
def dfs(graph, s, f, visited):
    q = [s]
    while len(q) > 0:
        current = q.pop()
        if current in visited:
            continue
        visited.update({current: None})
        f(current)
        for neigh in graph[current]:
            if not neigh in visited:
                q.append(neigh)

def build_graph():
    """
      A -- C 
      |    |  \
      B    E -- G
      |
      D -- F
    """
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'G'],
        'D': ['B', 'F'],
        'E': ['C', 'G'],
        'F': ['D'],
        'G': ['C']
    }

def process_node(node):
    print(node)

if __name__ == '__main__':
    graph = build_graph()
    visited = {}
    dfs(graph, 'A', process_node, visited)
