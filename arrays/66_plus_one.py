# First solved May 19, 2026

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # logic: start from the right side of the array, if it's 9, carry, otherwise just increment by one
        # O(1) space
        
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            # while there is a carry, set the digit at the current spot to be 0, and decrement to the next spot
            
            # bruh logic is cooked
            total = carry + digits[i]
            digits[i] = total % 10
            carry = total // 10
            i -= 1

        
        # if still a carry at the end of the loop, prepend a 1 to the front
        if carry:
            return [1] + digits
            
        return digits # note this syntax, be careful working with the arrays
        