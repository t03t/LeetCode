class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        q = deque()
        # get initial counts
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: # fresh
                    fresh_count += 1
                elif grid[i][j] == 2: # roten
                    q.append((i, j))
        if fresh_count == 0:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_elapsed = 0
        while q:
            min_elapsed += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check if in bounds and fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh_count -= 1
        return min_elapsed - 1 if fresh_count == 0 else -1
