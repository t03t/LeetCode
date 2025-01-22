from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for l in s:
                counts[ord(l) - ord('a')] += 1
            anagram_dict[tuple(counts)].append(s)
        return list(anagram_dict.values())
