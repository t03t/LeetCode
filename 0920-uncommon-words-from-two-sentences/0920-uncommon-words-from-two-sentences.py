from collections import Counter as c
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon = []
        w1, w2 = c(s1.split(" ")), c(s2.split(" "))
        for word in s1.split(" "):
            if word not in w2 and w1[word] <= 1:
                uncommon.append(word)
        for word in s2.split(" "):
            if word not in w1 and w2[word] <= 1:
                uncommon.append(word)
        return uncommon