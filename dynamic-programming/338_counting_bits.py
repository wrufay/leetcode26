# First solved June 3, 2026

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # get a refresher on dp basics first... crine

        # it's been a while like 2 weeks since i touched lc oops

        dp = [0] * (n + 1) # because inclusive of n. tells u in the question lol

        # base case, first element in the array always 0 because there are 0 ones in the binary representation of 0
        dp[0] = 0

        for i in range(1, n+1):
            dp[i] = dp[i // 2] + i % 2 # son i would not have gotten that i lowkey don't know how bianry works

        return dp



        