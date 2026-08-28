from collections import deque

grid = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

rows = len(grid)
cols = len(grid[0])

visited = [[False] * cols for _ in range(rows)]

directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1)    # right
]

def bfs(r, c):

    queue = deque()

    queue.append((r, c))
    visited[r][c] = True

    while queue:

        r, c = queue.popleft()

        print(grid[r][c], end=" ")

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))


bfs(0, 0)