class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        return all(ransom_count[char] <= mag_count[char] for char in ransom_count)