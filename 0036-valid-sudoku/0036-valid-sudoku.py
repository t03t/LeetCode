class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = len(board)
        # check rows
        for i in range(SIZE):
            seen = set()
            for j in range(SIZE):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])

        # check columns
        for i in range(SIZE):
            seen = set()
            for j in range(SIZE):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])

        # check squares
        starting_points = [ [0, 0], [0, 3], [0, 6],
                            [3, 0], [3, 3], [3, 6],
                            [6, 0], [6, 3], [6, 6] ]
        for i, j in starting_points:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in seen:
                        return False
                    elif board[row][col] != '.':
                        seen.add(board[row][col])
        return True