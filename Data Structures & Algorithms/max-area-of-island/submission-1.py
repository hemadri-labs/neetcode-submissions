from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        direct = [
            [-1,0], #up
            [1,0], #down
            [0,-1], #left
            [0,1] #right
        ]
        visited = set()
        maxarea = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    carea = 0
                    q = deque([(r,c)])
                    while q:
                        qr, qc = q.popleft()
                        visited.add((qr,qc))
                        carea += 1
                        for dr, dc in direct:
                            nr = dr + qr
                            nc = dc + qc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                                q.append((nr,nc))
                                visited.add((nr,nc))
                    maxarea = max(carea, maxarea)
        return maxarea

