# First solved May 6, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            cur_val = cur.val
            next_val = cur.next.val

            gcd_node = ListNode(math.gcd(cur_val, next_val))

            temp = cur.next
            cur.next = gcd_node
            gcd_node.next = temp
            
            cur = cur.next.next

        return head
        