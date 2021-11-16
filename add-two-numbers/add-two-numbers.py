# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # answer = None
        # head = answer
        answer = ListNode()
        head = answer
        cur = 0
        carry = 0
        while l1 or l2:
            if not l1:
                cur = l2.val + carry
                l2 = l2.next
            elif not l2:
                cur = l1.val + carry
                l1 = l1.next
            else:
                cur = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            carry = cur//10
            cur = cur%10
            print(cur)
#             if not head:
#                 current = ListNode(cur,None)
#                 head = answer
#                 answer.next = current
#                 print(head, "here")
            # else:
            current = ListNode(cur, None)
            print(answer, "also here?")
            answer.next = current
            answer = answer.next
            cur = 0
        if carry > 0:
            answer.next = ListNode(carry, None)
        return head.next