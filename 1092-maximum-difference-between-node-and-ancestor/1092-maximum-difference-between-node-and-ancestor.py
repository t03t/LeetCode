# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def fn(node, maxx, minn):
            if not node:
                return maxx - minn
            maxx = max(maxx, node.val)
            minn = min(minn, node.val)
            left = fn(node.left, maxx, minn)
            right = fn(node.right, maxx, minn)
            return max(left, right)
        return fn(root, root.val, root.val)