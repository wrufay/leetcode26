# First solved June 4, 2026

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:] # also don't even need to copy nums u can modify in place
        for i in range(1, len(nums)):
            # idea: at each i, check if extending the subarray is better than starting fresh at i. so we take the max of the sum and the sum plus current to extend
            if dp[i] < dp[i-1] + dp[i]:
                dp[i] = dp[i-1] + dp[i]
            #ok you can just say 
            # dp[i] = max(dp[i], dp[i-1] + dp[i]) 
            # i'm not used to using max. but its fine can write the if statment first and simplify after i guess c
        return max(dp)

        
        