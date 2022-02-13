class Solution:
    def checkString(self, s: str) -> bool:
        endofas = False
        for letter in s:
            if letter == "b" and not endofas:
                endofas = True
            elif letter == "a" and endofas:
                return False
        return True