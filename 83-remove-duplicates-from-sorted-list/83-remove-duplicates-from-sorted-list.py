# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        returnval = head
        prev = head
        if not head.next:
            return head
        head = head.next
        
        while head:
            if prev.val == head.val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
            
        return returnval
    