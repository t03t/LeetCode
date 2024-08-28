"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        node_stack = [(root, False)]
        while node_stack:
            cur, visited = node_stack.pop()
            if visited:
                res.append(cur.val)
            else:
                node_stack.append((cur, True))
                for child in reversed(cur.children):
                    node_stack.append((child, False))
        return res