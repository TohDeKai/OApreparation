# https://leetcode.com/problems/number-of-islands/description/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        have a visited matrix
        traverse through the grid
        if its 1 and not visited;
            add to visited
            islands += 1
            continue checking its left right up down
        """

        def extend(i, j):
            if grid[i][j] == "1":
                visited[i][j] = True
                if i + 1 < len(grid) and visited[i + 1][j] == False:
                    extend(i + 1, j)
                if j + 1 < len(grid[0]) and visited[i][j + 1] == False:
                    extend(i, j + 1)
                if i - 1 >= 0 and visited[i - 1][j] == False:
                    extend(i - 1, j)
                if j - 1 >= 0 and visited[i][j - 1] == False:
                    extend(i, j - 1)
            else:
                return

        visited = [[False for x in range(len(grid[0]))] for x in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                elem = grid[i][j]
                if elem == "1" and visited[i][j] == False:
                    res += 1
                    extend(i, j)
        return res
