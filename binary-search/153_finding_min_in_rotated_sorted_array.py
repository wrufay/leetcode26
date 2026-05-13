# First solved May 13, 2026

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search to find the rotation point, instead of a given target
        # each time try to narrow down the minimum

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]: # this means minimum of on the right of mid
                # so, set l to be mid + 1
                l = mid + 1
            else: # only have one case, otherwise the min is to the left of mid
                r = mid

        return nums[l] # goal is to get l to be the actual minumum
        