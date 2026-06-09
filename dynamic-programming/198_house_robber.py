# First solved June 8, 2026

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums[:] # make a copy

        # base case
        dp[0] = nums[0]
        
        if len(nums) > 1:
            # if only one element
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        # return last element
        return dp[-1]

        