# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #1. Recursive algorithm:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l2.val<l1.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        # else:
        #     if l1<l2:
        #         return l1
        #     else:
        #         return l2
        