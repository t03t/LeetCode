class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = [""] * numRows
 
        i = 0
        inc = 1
        for elem in s:
            rows[i] += elem
            if i == 0:
                inc = 1
            elif i == numRows - 1:
                inc = -1
            i += inc
        

        return "".join(rows)