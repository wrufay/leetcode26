# First solved May 3, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            # want: change the next of current to be previous, while keeping next of current in a temp variable
            temp = cur.next
            cur.next = prev
            # then iterate both pointers, prev goes to current and current goes to old cur.next which is stored in temp
            prev = cur
            cur = temp
        return prev

        