class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]": "["}
        accountability = []
        for letter in s:
            if letter in pairs.values():
                accountability.append(letter)
            elif letter in pairs.keys():
                if not accountability:
                    return False
                if accountability[-1]==pairs[letter]:
                    accountability.pop()
                else:
                    return False
        if len(accountability)==0:
            return True
        return False