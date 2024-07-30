class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter([letter for letter in s]) == Counter([letter for letter in t])