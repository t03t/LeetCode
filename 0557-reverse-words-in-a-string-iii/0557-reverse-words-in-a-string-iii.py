class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split(' ')
        for i in range(len(words)):
            res.append(''.join(list(words[i])[::-1]))
        return ' '.join(res)