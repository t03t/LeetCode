class Solution:
    def replaceDigits(self, s: str) -> str:
        l = None
        b = list(s)
        for i,c in enumerate(b):
            if c.isdigit():
                b[i]=chr(ord(l)+int(c))
            else:
                l = c
        return "".join(b)