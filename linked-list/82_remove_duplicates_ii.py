# First solved May 3, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # be careful of edge case where the head could be a duplicate, use dummy node
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        # idea: once you detect a repeated node, need to skip all instances of it, so use a nested loop (dw not quadratic time since we only moving cur forward)
        while cur and cur.next:
            if cur.val == cur.next.val:
                # is a duplicate, save that value in a temp, keep skipping
                target = cur.val

                # while the value is a repeat, iterate but don't relink anything yet
                while cur and cur.val == target:
                    cur = cur.next
                prev.next = cur # now we have skipped the repeats, relink prev to the new current node.
            else:
                # otherwise, iterate both as usual
                prev = cur
                cur = cur.next
        
        return dummy.next