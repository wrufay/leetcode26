# First solved May 11, 2026

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers, at either end of the array
        l = 0
        r = len(height) - 1
        max_water = 0

        while l != r:
            cur_water = (r - l) * min(height[l], height[r]) # get the amount of water at each step
            if cur_water > max_water:
                # if there is a new max, set it
                max_water = cur_water
                # ok could also just go like max_water = max(max_water, cur_water)
            
            # each iteration, move the index with the lesser water height towards the middle
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            
        return max_water
        