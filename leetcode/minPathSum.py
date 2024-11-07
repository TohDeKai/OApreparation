# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        go through the topmost row and leftmost row first
        get the sum of the path since you can only travel right and down
        for the rest of the cells
        you calculate the sum of path by taking minimum(top,left) + val
        starting from left to right, top to bottom
        """

        m = len(grid)
        n = len(grid[0])

        for j in range(n):
            if j!= 0:
                grid[0][j] += grid[0][j-1]

        for i in range(m):
            if i!= 0:
                grid[i][0] += grid[i-1][0]

        for i in range(m):
            for j in range(n):
                if i != 0 and j!= 0:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        return grid[m-1][n-1]