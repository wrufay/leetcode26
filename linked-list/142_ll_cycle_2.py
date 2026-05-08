# First solved May 8, 2026

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use set, store each node inside, as we traverse the linked list if that node appears in the set then that's where the cycle started
        nodes = set()
        cur = head
        while cur:
            if cur in nodes: # if the node is in the set
                return cur
            else:
                # add to the set
                nodes.add(cur)
                cur = cur.next
        return None


        