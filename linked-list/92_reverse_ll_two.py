# First solved May 6, 2026

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # algorithm/idea
        # create left_node and left_prev, advance them until we get to the desired left integer. we will use these when reattaching, so don't touch, then use typical reverse logic to perform reverse right - left + 1 times
        # reattach nodes


        left_node = head
        left_prev = None
        
        # advance both left_node and left_prev, we want left - 1 times since we start counting the nodes at 1
        for i in range(left - 1):
            left_prev = left_node
            left_node = left_node.next
        
        # reverse
        cur = left_node
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # by the end, cur is the rest of the list that wasn't reversed (it's the node after right-th node)
        # so we want to attach the node before where we started reversing (which is left_prev) to the head of the reversed list, which is prev
        # and then attach the tail of the reversed list, which is still left_node because that didn't change; still points at that although other stuff changed, attach that to cur.


        # don't forget this edge case: if left is 1, then left_prev stays as None so we cannot access left_prev.next. in this case, head becomes prev
        if left_prev:
            left_prev.next = prev
        else:
            head = prev
        left_node.next = cur

        return head # in all other cases, head does not change.

        