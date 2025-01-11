class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def dfs(row, col):
            q = deque()
            q.append((row, col))
            seen.add((row, col))
            while q:
                r, c = q.pop()
                adjacents = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dx, dy in adjacents:
                    rx, ry = r + dx, c + dy
                    if rx in range(rows) and ry in range(cols) and (rx, ry) not in seen and grid[rx][ry] == "1":
                        q.append((rx, ry))
                        seen.add((rx, ry))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    islands += 1
        return islands