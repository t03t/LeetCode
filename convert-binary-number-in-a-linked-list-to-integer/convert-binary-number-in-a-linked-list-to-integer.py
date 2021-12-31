# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        counter = head
        count = 0
        while counter:
            count += 1
            counter = counter.next
        decimal = 0
        multiply = 2**(count-1)
        while head:
            decimal += multiply * head.val
            multiply //= 2
            head = head.next
        return decimal
        