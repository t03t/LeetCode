class Solution():
    def reverseStr(self, s: str, k: int) -> str:
        out = list(s)
        for i in range(0,len(s),2*k):
            out[i:i+k] = s[i:i+k][::-1]
        return "".join(out)