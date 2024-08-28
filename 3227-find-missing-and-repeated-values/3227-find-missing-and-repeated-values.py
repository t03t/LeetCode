class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = -1
        seen = set()
        SIZE = len(grid)
        for row in range(SIZE):
            for col in range(SIZE):
                if grid[row][col] in seen:
                    repeated = grid[row][col]
                seen.add(grid[row][col])
        all_numbers = set(range(1, SIZE * SIZE + 1))
        missing = list(all_numbers - seen)[0]
        return repeated, missing