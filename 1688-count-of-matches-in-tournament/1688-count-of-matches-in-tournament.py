class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
        winner = n
        c =0
        while winner != 1:
            c+=1
            if winner%2 == 0:
                winner = winner/2
            else:
                winner = ((winner-1)/2) + 1
        return c