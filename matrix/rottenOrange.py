from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        time = 0
        fresh = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)] 

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        # BFS
        while queue and fresh > 0:

            for _ in range(len(queue)):
                r , c = queue.popleft()

                for dr , dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row and 0 <= nc < col:


                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            fresh -= 1

            time += 1

        if fresh == 0:
            return time

        return -1    



        




        