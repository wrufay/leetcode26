# First solved May 11, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = prev.next
        sum = 0

        while cur:
            if cur.val != 0:
                sum += cur.val
            else:
                node = ListNode(sum)
                prev.next = node
                prev = node
                sum = 0
            cur = cur.next
        
        return head.next
        