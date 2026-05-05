
# First solved May 4, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # binary to decimal: multiply each bit by 2 to the power of its position from the right starting at 0

        # either traverse backwards or know the length first

        # get length of linked list so we know which pos to start at
        pos = 0
        temp = head
        while head:
            pos += 1
            head = head.next

        result = 0
        head = temp # reset to beginning
        while head:
            pos -= 1
            result += head.val * (2 ** pos)
            head = head.next

        return result


        