# https://leetcode.com/problems/max-area-of-island/description/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        traverse through the grid
        if its 1, start a count and count number of 1s
        and then traverse through neighbouring grid and convert to 0

        continue and find max count
        """
        res = 0

        def traverse(i, j):
            if (
                i < len(grid)
                and i >= 0
                and j < len(grid[0])
                and j >= 0
                and grid[i][j] == 1
            ):
                grid[i][j] = 0
                return (
                    1
                    + traverse(i + 1, j)
                    + traverse(i - 1, j)
                    + traverse(i, j + 1)
                    + traverse(i, j - 1)
                )
            else:
                return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = traverse(i, j)
                    res = max(res, count)

        return res
