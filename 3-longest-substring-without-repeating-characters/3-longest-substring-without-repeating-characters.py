class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charSet = set()
        l = 0
        for r, num in enumerate(s):
            while num in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(num)
            longest = max(longest, r-l +1 )
        return longest