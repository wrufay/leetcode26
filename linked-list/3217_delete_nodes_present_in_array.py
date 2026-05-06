# First solved May 4, 2026

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # since we don't care about duplicates and want a quick lookup in the array, first convert to a set
        nums_set = set(nums) # secretly like a hash table

        # logic / idea: use prev pointer for deleting, iterate and check if each one is in the nums set; returning head so make a dummy 

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            if cur.val in nums_set:
                # remove the current node as usual
                prev.next = cur.next
            else:
                # otherwise, advance both prev and cur pointers
                prev = cur
            # also advance cur in both cases
            cur = cur.next
                

        return dummy.next
        