class Solution:
    def firstUniqChar(self, s: str) -> int:
        unicity = Counter(s)
        for letter in s:
            if unicity[letter] == 1:
                return s.index(letter)
        return -1