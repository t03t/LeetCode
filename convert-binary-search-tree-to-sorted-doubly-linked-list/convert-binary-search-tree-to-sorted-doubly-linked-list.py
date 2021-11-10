"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = None
        tail = None
        def helper(cur):
            nonlocal head, tail
            if cur:
                helper(cur.left)
                if tail:
                    tail.right = cur
                    cur.left = tail
                else:
                    head = cur
                tail = cur
                helper(cur.right)
        
        if not root:
            return None
        helper(root)
        head.left = tail
        tail.right = head
        return head