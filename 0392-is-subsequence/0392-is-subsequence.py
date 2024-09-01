class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Using two pointer approach
        if not s:
            return True
        a, b = 0, 0
        while b < len(t) and a < len(s):
            lA = s[a]
            lB = t[b]
            if lA == lB:
                a += 1
                b += 1
            else:
                b += 1
        if a == len(s):
            return True
        return False