# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head = 1
        # head.next = 2
        # reverse = head.next
        if not head:
            return 
        cur = head
        nxt = cur.next
        while nxt:
            prev = cur
            cur = nxt
            nxt = cur.next
            cur.next = prev
        head.next = None
        return cur
        