# First solved May 12, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # helper function that reverses a linked list, returning the head

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we have to start adding from the right, so reverse both lists
        l1_rev = self.reverse(l1)
        l2_rev = self.reverse(l2)

        # setup the list we are making with dummy node, make sure when you reverse it, skip the dummy so the new head is without the dummy
        dummy = ListNode()
        cur = dummy 

        # then add each number, using same carry logic
        carry = 0
        while l1_rev or l2_rev or carry:
            val1 = l1_rev.val if l1_rev else 0
            val2 = l2_rev.val if l2_rev else 0
            
            sum = val1 + val2 + carry

            carry = sum // 10
            node = ListNode(sum % 10)
            cur.next = node
            cur = cur.next

            if l1_rev: l1_rev = l1_rev.next
            if l2_rev: l2_rev = l2_rev.next

        return self.reverse(dummy.next)

        



        