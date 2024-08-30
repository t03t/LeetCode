class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        bijection = {}
        for letter, word in zip(pattern, words):
            print(letter, word, bijection, bijection.values())
            if letter in bijection and bijection[letter] != word:
                return False
            if letter not in bijection and word in bijection.values():
                return False
            elif letter not in bijection and word not in bijection.values():
                bijection[letter] = word
        return True