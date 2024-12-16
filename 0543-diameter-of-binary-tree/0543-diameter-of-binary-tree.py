# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        # diameter is the sum of max left length and max right length
        def maxDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        maxDepth(root)
        return self.res