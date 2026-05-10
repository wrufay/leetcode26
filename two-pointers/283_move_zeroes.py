# First solved May 10, 2026

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1
        
        # set the zeroes back, looping from w to the end
        while w < len(nums):
            nums[w] = 0
            w += 1


        