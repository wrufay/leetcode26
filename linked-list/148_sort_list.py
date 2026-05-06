# First solved May 6, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head == None or head.next == None:
            # if list is empty, return empty list. if only one node, list is already sorted; return itself
            return head
        else:
            # get middle for merge sort
            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # slow is at the middle, prev pointing to the node right before slow so we set that next to be none, splitting the lists.
            prev.next = None
            return self.merge(self.sortList(head), self.sortList(slow))
        
    # Helper function to merge two sorted linked lists, returning the head of the resulting list
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        
        if l1: cur.next = l1
        if l2: cur.next = l2

        return dummy.next
        

        