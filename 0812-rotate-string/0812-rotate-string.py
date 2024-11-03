class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        max_shifts = len(s)
        for i in range(max_shifts):
            s = s[1:]+s[0]
            if s == goal:
                return True
        return False