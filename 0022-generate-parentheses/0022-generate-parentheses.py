class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paranthesis = []
        res = []
        def backTrack(opened, closed):
            if opened == closed == n:
                res.append("".join(paranthesis))
                return
            if opened < n:
                paranthesis.append("(")
                backTrack(opened+1, closed)
                paranthesis.pop()
            if closed < opened:
                paranthesis.append(")")
                backTrack(opened, closed + 1)
                paranthesis.pop()
        backTrack(0, 0)
        return res