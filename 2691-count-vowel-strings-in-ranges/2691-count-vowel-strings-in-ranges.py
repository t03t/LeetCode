class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_words = []
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                if vowel_words:
                    vowel_words.append(vowel_words[-1] + 1)
                else:
                    vowel_words.append(1)
            else:
                if vowel_words:
                    vowel_words.append(vowel_words[-1])
                else:
                    vowel_words.append(0)
        query_cache = {}
        res = []
        print(vowel_words)
        for l, r in queries:
            print(r)
            if (l, r) in query_cache:
                res.append(query_cache[(l, r)])
            else:
                if l == 0:
                    count = vowel_words[r]
                else:
                    count = vowel_words[r] - (vowel_words[l - 1])
                res.append(count)
                query_cache[(l, r)] = count
        return res
        

        