class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        dir = [
            [0, 1],
            [-1, 0],
            [1, 0],
            [0, -1]
        ]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1" or (r,c) in visited:
                    continue
                islands += 1
                visited.add((r,c))
                q = deque([(r,c)])

                while q:
                    cr, cc = q.popleft()

                    for dr, dc in dir:
                        nr = cr + dr
                        nc = cc + dc
                        if (0 <= nr < rows 
                            and 0 <= nc < cols 
                            and grid[nr][nc] == "1" 
                            and (nr,nc) not in visited):
                            visited.add((nr,nc))
                            q.append((nr,nc))

        return islands


                    
