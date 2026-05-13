# First solved May 13, 2026

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # straight binary search muscle memory
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]: # target is on the right
                l = mid + 1
            else:
                r = mid - 1
            
        return -1
        