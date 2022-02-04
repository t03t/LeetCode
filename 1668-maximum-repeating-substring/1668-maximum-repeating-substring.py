class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        original = word
        while word in sequence:
            count+=1
            word+=original
        return count