class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = set()
        for letter in s:
            if letter in dic:
                return letter
            dic.add(letter)
        return ""