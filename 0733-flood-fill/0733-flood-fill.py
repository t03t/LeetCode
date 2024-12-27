class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # sr - starting row, sc = starting column
        r, c = len(image), len(image[0])
        start = image[sr][sc]
        if start == color:
            return image
        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != start:
                return
            image[i][j] = color
            # dfs all the surrounding 
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        dfs(sr, sc)
        return image


