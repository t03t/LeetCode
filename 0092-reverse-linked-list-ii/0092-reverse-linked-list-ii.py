# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # part 1 - navigate to left node
        dummy = ListNode(0, head)
        left_end, cur = dummy, head
        for _ in range(left - 1):
            left_end, cur = cur, cur.next
        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        left_end.next.next = cur
        left_end.next = prev
        return dummy.next