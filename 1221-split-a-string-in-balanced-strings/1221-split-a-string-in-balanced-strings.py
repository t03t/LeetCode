class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        splits = 0 
        for letter in s:
            if letter == "R":
                balance += 1
            elif letter == "L":
                balance -= 1
            if balance == 0:
                splits += 1
        return splits