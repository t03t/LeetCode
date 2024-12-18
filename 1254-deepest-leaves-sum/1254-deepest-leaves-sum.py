# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root,])
        while queue:
            curr_queue = queue
            # do some logic here for the current level
            queue = deque()

            for node in curr_queue:
                # put the next level onto the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum([node.val for node in curr_queue])