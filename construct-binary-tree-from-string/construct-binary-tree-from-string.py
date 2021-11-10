# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        def builder(Iter):
            number = "" #in the case of negatives
            nxt = next(Iter)
            while (nxt) not in [")","("]:
                number += nxt
                nxt=next(Iter)
                
                
            node = TreeNode(int(number))
            
            if nxt == '(':
                node.left = builder(Iter)
                
                if next(Iter) == '(':
                    
                    node.right = builder(Iter)
                    next(Iter)
                    
            return node

        return builder(iter(s + ')')) if s else None
                    
                        
                
        
#         def removeBrackets(s):
#             return s[1:-1]