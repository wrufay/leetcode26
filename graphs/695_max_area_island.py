# First solved June 11, 2026

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # should be a similar idea as the previous island question (200) but we are tracking the size of islands instead of just counting them

        # inside dfs we should be returning a number instead of boolean like last time. and on the outside loop we take the maximum each time. then return that outside of the loop

        # oh also look closely this question uses ints!

        max_size = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            # base case, return 0 if it's outside of the range
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            
            # otherwise, mark it as seen and continue the dfs, as well as increase the current sum
            grid[i][j] = 0

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_size = max(dfs(i, j), max_size)
            

        return max_size

        
        