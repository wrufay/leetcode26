# First solved May 14, 2026

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # better solution; sorting the list first and using the index, because the index of each number is exactly how many numbers in the sorted array have a value smaller than it.
        # to keep the original order tho we need to use a hashmap, and keep a copy of the original nums array to be able to lookup the index for each one
        sorted_nums = sorted(nums)
        my_map = {}

        for i in range(len(nums)):
            # also need to only add into the map if it doesn't exist already; otherwise the index will update which would not be correct for duplicated values

            if sorted_nums[i] not in my_map:
                # key = value (nums[i]), value = index (i)
                my_map[sorted_nums[i]] = i
        
        # loop through nums array again, changing the value to its index by looking up in the hashmap
        for i in range(len(nums)):
            nums[i] = my_map[nums[i]]

        return nums
