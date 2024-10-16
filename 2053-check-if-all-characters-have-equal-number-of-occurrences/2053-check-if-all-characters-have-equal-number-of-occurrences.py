class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freqs = Counter()
        for letter in s:
            freqs[letter] += 1
        return len(set(freqs.values())) == 1
        