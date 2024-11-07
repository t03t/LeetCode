# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur):
            if not node:
                return False
            if node.left == None and node.right == None:
                return (cur + node.val) == targetSum
            cur += node.val
            left = dfs(node.left, cur)
            right = dfs(node.right, cur)
            return left or right
        return dfs(root, 0)
