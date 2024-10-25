class Solution:
    def makeGood(self, s: str) -> str:
        res = [s[0]]
        for letter in s[1:]:
            if res and res[-1] != letter and letter.lower() == res[-1].lower():
                res.pop()
            else:
                res.append(letter)
        return "".join(res)