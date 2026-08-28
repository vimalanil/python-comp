def dfs(r, c):

    # 1. Check boundary
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    # 2. Check invalid / already visited
    if grid[r][c] == 0:
        return

    # 3. Mark as visited
    grid[r][c] = 0

    # 4. Go in 4 directions
    dfs(r - 1, c)   # up
    dfs(r + 1, c)   # down
    dfs(r, c - 1)   # left
    dfs(r, c + 1)   # right