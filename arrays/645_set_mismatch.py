# First solved May 14, 2026
# Quest: DSA - Array II Q1)

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        # while iterating through nums array, add it to the set. if it's already in the set, that's the duplicated one. 

        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)

        # find missing one: loop from 1 to n, if that num is not in the set, then that's the missing one
        for i in range(1, len(nums) + 1): # to length plus one because starting at 1
            if i not in seen:
                result.append(i)
                break
        return result
        

        
        