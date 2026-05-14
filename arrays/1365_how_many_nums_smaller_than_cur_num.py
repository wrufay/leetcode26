# First solved May 14, 2026
# Quest: DSA - Array II Q2)
# More efficient solution in hashsets category

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # intuitive solution: using two for loops; for each nums[i], calculate with another loop comparing nums[i] with nums[j] assuming j=/i, store this value in an array; can solve faster by sorting the array first but we try this intuitive method
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            result.append(count)

        return result
                
                    

        