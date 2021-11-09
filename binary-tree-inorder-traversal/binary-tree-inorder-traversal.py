# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, l):
            if root:
                if root.left:
                    helper(root.left, l)
                l.append(root.val)
                if root.right:
                    helper(root.right, l)
        visit = []
        helper(root, visit)
        return visit
        
        
        