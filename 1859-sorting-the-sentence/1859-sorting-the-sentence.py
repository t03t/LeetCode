from collections import defaultdict
class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = defaultdict()
        for word in s.split(" "):
            sentence[word[-1]]=word[:-1]
        sentence= [sentence[key] for key in sorted(sentence)]
        return " ".join(sentence)