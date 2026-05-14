# First solved May 13, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # slow fast pointers, reverse second half, compare each node sum and find teack the max.
        max_sum = 0

        cur = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now we reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        mid = prev
        
        # now iterate and compare the max of each sum of nodes
        while cur and mid: 
            cur_sum = cur.val + mid.val
            if cur_sum > max_sum:
                max_sum = cur_sum
            
            cur = cur.next
            mid = mid.next
        
        return max_sum
        