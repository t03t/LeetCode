# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = collections.deque()
        stack.append(root)
        levels = []
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            if level:
                levels.append(level)
        levels.reverse()
        return levels