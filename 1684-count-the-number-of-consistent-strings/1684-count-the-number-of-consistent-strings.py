class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cons = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                cons+=1
        return cons
        