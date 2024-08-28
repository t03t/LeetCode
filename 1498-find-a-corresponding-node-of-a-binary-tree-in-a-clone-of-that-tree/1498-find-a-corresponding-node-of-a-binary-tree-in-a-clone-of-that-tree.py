# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        target_found = original == target or not original
        if target_found:
            return cloned
        copy = self.getTargetCopy(original.left, cloned.left, target)
        if copy:
            return copy
        return self.getTargetCopy(original.right, cloned.right, target)