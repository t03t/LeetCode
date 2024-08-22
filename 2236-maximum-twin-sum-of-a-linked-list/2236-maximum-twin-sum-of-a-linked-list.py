# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return True
        # O(1) Space
        cur = head  # This is your 'cur' pointer
        mid_node = head  # This acts as the slow pointer
        fast = head  # This acts as the fast pointer
        
        while fast and fast.next:
            mid_node = mid_node.next  # slow pointer moves one step
            fast = fast.next.next  # fast pointer moves two steps
        # reverse mid_node through end
        cur = mid_node
        prev = None
        while cur:
            # a -> b -> c
            # ^    ^ 
            # |    |
            #cur  tmp 
            tmp = cur.next
            cur.next = prev
            #None <-- a    b -> c
                    # ^    ^ 
                    # |    |
                    #cur  tmp
            prev = cur
            cur = tmp
            #None <-- a    b -> c
                    # ^    ^ 
                    # |    |
                    #prev  cur
        max_sum = 0
        while prev and head:
            if max_sum < prev.val + head.val:
                max_sum = prev.val + head.val
            prev = prev.next
            head = head.next
        return max_sum