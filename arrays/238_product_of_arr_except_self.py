# First solved June 7, 2026

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 3 loops - get everything left of nums[i] multiplied by everything on the left, same thing with the right, and then multiply each side by each other


        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            # starting with the first index
            left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums) - 2, -1, -1):
            # starting with the first index
            right[i] = nums[i+1] * right[i+1]


        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]

        return result
        
        