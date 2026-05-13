# First solved May 13, 2026

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(logn) tells us we need to use binary search!

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]: # target is on the right of mid
                # so we set the new left to be mid + 1
                l = mid + 1
            else: # target is on the left of mid
                # so we set the new right to be mid - 1
                r = mid - 1

        return l

        # mistakes at first: make sure you use while l <= r so they wont overlap 
        # okay and also if the number is not found, l is going to be the index it needs to be inserted at; not l + 1. (weak spot is indices, prob need to work on this! - actually write it out, see what's right based on patterns instead of just guessing.)

        