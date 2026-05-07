# First solved May 7, 2026

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        map = {}

        # set the actual number to be the key, index is the value
        for i in range(len(nums)):
            # check before adding to the map
            complement = target - nums[i]

            if complement in map:
                result.append(i)
                # lookup the index of the complement value and append it to result
                result.append(map[complement])

            cur = nums[i]
            map[cur] = i 

        return result