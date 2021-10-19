# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        counts = collections.Counter()
        while head:
            if counts[head]==1:
                return True
            counts[head] += 1
            head = head.next
        return False
        