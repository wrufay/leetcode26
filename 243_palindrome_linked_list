# First solved May 3, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # idea: find the middle, reverse the second half, and compare those two linked lists (first half with reversed second half)
        # first find middle using slow/fast pointer method
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # note - slow is the middle node.

        list2 = None # this is the reversed second half of the list
        # reverse everything in the same list, then compare with loop
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # now prev is the head of the second half, and head is still pointing at the head of the first half. (can use head in the loop because we don't need to return it at the end)
        while prev:
            if prev.val != head.val:
                return False
            else:
                prev = prev.next
                head = head.next
        return True
        