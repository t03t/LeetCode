class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(list(s.split(" "))[:k])