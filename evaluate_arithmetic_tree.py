class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate(node):
    if not is_operator(node.val):
        return node.val
    return ops[node.val](
        evaluate(node.left),
        evaluate(node.right)
    )

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def is_operator(c):
    return c in ops

"""
    Suppose an arithmetic expression is given
    as a binary tree.
    Each leaf is an integer and each internal node
    is one of '+', '-', '*', or '/'.

    Given the root to such a tree,
    write a function to evaluate it.

    For example, given the following tree:
            *
          /   \
         +     +
        / \   / \
       3   2 4   5

    Evaluates to 45.
"""
def build_tree():
    root = node('*')
    root.left = node('+')
    root.right = node('+')
    root.left.left = node(3)
    root.left.right = node(2)
    root.right.left = node(4)
    root.right.right = node(5)
    return root

if __name__ == '__main__':
    root = build_tree()
    print('Result: {}'.format(evaluate(root)))
