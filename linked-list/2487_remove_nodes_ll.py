# First solved May 11, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    # helper function that reverses a linked list and return the head of the reversed list
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = self.reverse(head) # reverse the list so we can work from right to left, finding the max value

        prev = reversed
        cur = prev.next
        max = prev.val

        while cur:
            if cur.val >= max: # update the max value
                max = cur.val
                prev = cur
                cur = cur.next
            else: # remove 
                cur = cur.next
                prev.next = cur # just iterate, skipping the current node

        return self.reverse(reversed)
        
        