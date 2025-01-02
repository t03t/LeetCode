# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        res = []
        q.append(root)
        while q:
            avg_sum, c, avg = 0, 0, 0
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    avg_sum += node.val
                    c += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg = avg_sum / c
            res.append(avg)
        return res

