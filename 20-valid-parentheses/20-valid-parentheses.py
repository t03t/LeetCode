class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]": "["}
        accountability = []
        for letter in s:
            if letter in "({[":
                accountability.append(letter)
            elif letter in ")}]":
                if not accountability:
                    return False
                if accountability[-1]==pairs[letter]:
                    accountability.pop()
                else:
                    return False
        if len(accountability)==0:
            return True
        return False