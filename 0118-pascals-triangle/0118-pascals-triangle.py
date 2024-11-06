class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prev_ = self.generate(numRows - 1)
        prev = prev_[-1]
        cur = [1]
        for i in range(1, numRows - 1):
            cur.append(prev[i - 1] + prev[i])
        cur.append(1)
        prev_.append(cur)
        return prev_
