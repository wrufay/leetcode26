# First solved May 24, 2026

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # same idea as climbing stairs, but this time, since we are trying to get dp[i] as the min cost to get to the ith step and step off, calc with the last two

        dp = [0] * len(cost)

        # base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            # the minumum cost at each i is the current cost and the min of the previous two
        
        return min(dp[-1], dp[-2])
        # final min cost will be the min of the final two entries, either went two steps or one the last time
        
        
        