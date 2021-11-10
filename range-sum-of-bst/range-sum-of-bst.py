# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int) -> int:
        maxSum = []
        
        def sumTree(root):
            nonlocal maxSum
            if root:
                if l <= root.val <= h:
                    maxSum.append(root.val)

                if root.val > l:
                    sumTree(root.left)
                    
                if root.val < h:
                    sumTree(root.right)
        
        sumTree(root)
        return sum(maxSum)