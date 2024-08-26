# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle using slow and fast
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # rev
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # merge two sorted
        l, r = head, prev
        while r.next:
            l.next, l = r, l.next
            r.next, r = l, r.next