# First solved May 4, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use slow/fast pointers where fast begins n steps away from slow, that way when fast reaches the end, slow will be at the nth node, and we can delete it using prev pointer method as usual

        # returning head, so have a dummy
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        slow = head
        fast = head

        # first, get fast to be at the nth node using loop, advance fast n times 
        for i in range(n):
            fast = fast.next
        
        # then advance both + prev at the same rate (one at a time)
        while fast: # note, only need fast to be not null since we are not advancing fast twice unlike the finding middle one; otherwise it would stop early, would have needed to change the n in the loop to n-1 for it to work.
            fast = fast.next
            prev = slow
            slow = slow.next

        # remove that pointer that we are stopped at; slow is at the node we want to delete.
        prev.next = slow.next
        return dummy.next
        