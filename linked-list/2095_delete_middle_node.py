

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use slow/fast pointers, need another pointer behind slow to keep track

        # also need to return the head, so keep track
        slow = head
        fast = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # now, slow is at the middle of the list
        prev.next = slow.next
        
        return dummy.next
        