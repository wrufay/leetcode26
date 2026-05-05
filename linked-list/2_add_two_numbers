# First solved May 5, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode() # build the list, dummy so we can return head later
        tail = dummy # need a tail pointer so we can attach to the end

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry = sum // 10 # this will carry over
            cur_digit = sum % 10 # only the digit we are going to link

            # make a new node with digit, link it to the tail
            cur_node = ListNode(cur_digit)
            tail.next = cur_node
            tail = cur_node # update the tail

            # iterate both lists
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        