class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count, allowed = 0, set(allowed)
        for word in words:
            if set(word).issubset(allowed):
                count += 1
        return count