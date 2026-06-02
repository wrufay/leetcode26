# First solved May 24, 2026

class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n <= 2: return n

        # use bottom-up approach
        dp = [0] * (n + 1) # make arrays with all 0

        # set up the base cases
        dp[1] = 1
        dp[2] = 2

        # calculate the rest based on the previous answers
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]