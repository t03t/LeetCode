class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempset = {}
        longest = 0
        start = 0
        if len(s)<=1:
            return len(s)
        for i, letter in enumerate(s):
            if letter in tempset and start <= tempset[letter]:
                start = tempset[letter] +1
            else:
                longest = max(longest, i-start+1)
            tempset[letter]=i
        return longest