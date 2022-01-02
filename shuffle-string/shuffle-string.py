class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for ind,letter in zip(indices, list(s)):
            d[ind]=letter
        return ("".join(d[i] for i in sorted(d)))