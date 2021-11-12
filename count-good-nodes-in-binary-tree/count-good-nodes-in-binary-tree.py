# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(maxsofar, node):
            nonlocal count
            if not node:
                return
            if node.val>=maxsofar:
                count += 1
            helper(max(node.val, maxsofar), node.right)
            helper(max(node.val, maxsofar), node.left)
        if not root:
            return 0
        count = 0
        helper(float("-inf"), root)
        return count
            