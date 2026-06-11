# First solved June 11, 2026

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # use graphs.

        # idea: start by going through each cell in the grid. if we come accross a 1, we call a DFS helper whcih does depth first search recursively

        # first we have to get m and n (number of rows and cols)
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # use a closure for the helper function so we don't have to pass in the rows and columns

        def dfs(i, j):
            # base case, return and stop counting whenever we step into water aka are out of bounds or we reach water (only continue recursing if we are in bounds and are on a land)

            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return

            # mark as seen otherwise
            grid[i][j] = "0"
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1 # increase whenever we see a new one
                    # yeah i lwk got that put it in the right spot nice trust the instinct i guess. hahaaaahha

                    # basically we can pass invalid indices into here, the helper will sort it out. that is the logic.
                    dfs(i, j)

        return count

        