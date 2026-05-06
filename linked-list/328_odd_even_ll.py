# First solved May 6, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        first_even = cur.next if cur else None # handle this edge case
        
        while cur and cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            cur = cur.next
            temp.next = cur.next
        
        if cur: cur.next = first_even # don't forget the edge case
        return head
        