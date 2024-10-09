class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_c = 0
        res = 0
        for par in s:
            if par == '(':
                left_c += 1
            else:
                left_c -= 1
                if left_c < 0:
                    left_c = 0
                    res += 1
        return left_c + res