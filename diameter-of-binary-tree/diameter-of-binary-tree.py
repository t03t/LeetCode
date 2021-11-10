# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        
        def helper(node):
            nonlocal maxLen
            if node:
                left = helper(node.left)
                right = helper(node.right)
                maxLen = max(maxLen, left + right)
                
                return max(left + 1, right + 1)
            
            return 0
        
        helper(root)
        return maxLen