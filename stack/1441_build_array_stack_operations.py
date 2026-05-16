# First solved May 15, 2026
# Quest: DSA - Stack Q1)

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # if keep - push. if not keeping - push and pop. want to make the stack the same as the target.

        result = [] # store the operation
        s = set()

        for num in target:
            s.add(num)

        for i in range(1, n + 1): # loop through from 1 to n
            if not s: # if the set is empty, stop because we've finished building the stack
                break
            
            if i in s:
                result.append("Push")
                s.remove(i) # don't forget to remove the item from the set when we've put it on the stack
            else:
                result.append("Push")
                result.append("Pop")

        return result
            



        