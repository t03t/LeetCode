# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float('inf')
        low = float('-inf')
        
        def isValid(node, minimum, maximum):
            nonlocal high, low
            if not node:
                return True
            if not minimum < node.val < maximum:
                return False
            return isValid(node.left, minimum, node.val) and isValid(node.right, node.val, maximum)
        
        return isValid(root,low, high)