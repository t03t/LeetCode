class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(Counter(ransomNote)[char] <= Counter(magazine)[char] for char in Counter(ransomNote))