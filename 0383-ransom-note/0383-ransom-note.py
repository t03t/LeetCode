class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        return all(ransom_count[char] <= Counter(magazine)[char] for char in ransom_count)