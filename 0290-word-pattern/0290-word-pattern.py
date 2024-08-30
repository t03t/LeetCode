class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        bijection = {}
        for letter, word in zip(pattern, words):
            if letter in bijection:
                if bijection[letter] != word:
                    return False
            else:
                if word in bijection.values():
                    return False
                else:
                    bijection[letter] = word
        return True