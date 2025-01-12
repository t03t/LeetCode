from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "_" + word[i+1:]
                nei_list[pattern].append(word)
        q = deque([beginWord])
        seen = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # get potential patterns of the word
                for j in range(len(word)):
                    potential_pattern = word[:j] + "_" + word[j+1:]
                    for nei in nei_list[potential_pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        return 0