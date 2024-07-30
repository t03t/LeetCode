class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort(word: str):
            return ''.join(sorted(list(word)))
        groups = defaultdict(list)
        for word in strs:
            sorted_word = sort(word)
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        return groups.values()
