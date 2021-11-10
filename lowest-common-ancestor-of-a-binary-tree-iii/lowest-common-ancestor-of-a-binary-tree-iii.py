"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        lcaSet = set()
        
        while p:
            lcaSet.add(p)
            p = p.parent
        
        while q:
            if q in lcaSet:
                return q
            q = q.parent