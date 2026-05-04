from typing import Optional
# First solved 05/04/26

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Helper functions 

    # Reverse a linked list and returns the head
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
            
    # Returns the middle node of a linked list
    # Stops early for odd lengths
    def middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Idea: Find the middle, reverse the second half and interleave the two linked lists.
        mid = self.middle(head)
        second = self.reverse(mid)
        # when you reverse the second half, automatically first will be pointing at the first half of the list (breaking that connection in the middle)
        first = head

        # interleave first and second
        while first and second:
            first_temp = first.next
            first.next = second
            second_temp = second.next
            second.next = first_temp

            # advance both
            first = first_temp
            second = second_temp




    