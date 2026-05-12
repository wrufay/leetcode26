# First solved May 11, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    # helper function to reverse a linked list, returning the head of the new list (good review, make sure you know the logic solid)
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = self.reverse(head) # reverse the list
        
        cur = reversed
        carry = 0
        prev = None # just so we can attach the new node at the end, have a pointer right behind current
        while cur:
            doubled = (cur.val * 2) + carry # add carry right after doubling (carry is from the previous calculation)
            carry = doubled // 10
            cur.val = (doubled % 10)
            prev = cur 
            cur = cur.next
        if carry:
            node = ListNode(carry)
            prev.next = node
        
        return self.reverse(reversed)


        