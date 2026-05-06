# First solved May 6, 2026

from typing import Optional
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head = self.head
        # get length
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next
        
        cur = head
        random_int = random.randint(0, list_len - 1)
        for i in range(random_int):
            cur = cur.next
        return cur.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()