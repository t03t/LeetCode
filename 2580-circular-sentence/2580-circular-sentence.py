class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence:
            return False
        # if len(sentence.split(" ")) == 1:
        #     if sentence[-1] != sentence[0]:
        #         return False
        prev = sentence.split(" ")[-1]
        for word in sentence.split(" "):
            if prev and prev[-1] != word[0]:
                return False
            prev = word
        return True