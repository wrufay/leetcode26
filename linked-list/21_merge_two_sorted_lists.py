# First solved April 30, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        # need a tail for this one since we want to add to the end but like return the head at the end.
        head = ListNode()
        tail = head

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            # don't forget to advance the tail aka result
            tail = tail.next
    
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        

        # returning next since the first node was a dummy/placeholder
        return head.next

        