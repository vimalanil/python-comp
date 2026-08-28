class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        land = 0

        def dfs(r, c):

            # outside the matrix
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            # water / already visited
            if grid[r][c] == "0":
                return

            # mark as visited
            grid[r][c] = "0"

            # four directions
            dfs(r - 1, c)   # up
            dfs(r + 1, c)   # down
            dfs(r, c - 1)   # left
            dfs(r, c + 1)   # right

        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1":
                    land += 1
                    dfs(i, j)

        return land