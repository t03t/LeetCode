class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter()
        for edge in edges:
            for e in edge:
                c[e]+=1
        return c.most_common(1)[0][0]