class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            letter = s[r]
            while letter in seen:
                seen.remove(s[l])
                l+= 1
            seen.add(letter)
            res = max(res, r - l + 1)
        return res