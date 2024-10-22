class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqs = Counter(text)

        balloon = Counter("balloon")

        possibilities = []
        for char in balloon:
            possibilities.append(freqs[char]//balloon[char])
        return min(possibilities)