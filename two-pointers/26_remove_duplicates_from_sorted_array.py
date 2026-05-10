
# First solved May 10, 2026

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        for r in range(1, len(nums)):
            if nums[w] != nums[r]:
                w += 1
                nums[w] = nums[r]
        return w + 1
            


        

        
            


        

        