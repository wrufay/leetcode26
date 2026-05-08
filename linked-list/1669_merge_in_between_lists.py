# First solved May 8, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # take a pointer, iterate it until right before the a-th node
        cur = list1
        for i in range(a-1):
            cur = cur.next
        
        temp = cur
        # iterate cur until we get to before the b'th node
        for i in range(b - a + 2):
            temp = temp.next
        
        # attach list2 to cur
        cur.next = list2
        # iterate until we get to the end of the list
        while cur.next:
            cur = cur.next
        # attach the kept part to the end
        cur.next = temp
        return list1

        