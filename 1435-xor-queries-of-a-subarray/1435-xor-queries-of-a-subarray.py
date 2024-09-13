class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pref[i + 1] = pref[i] ^ arr[i]
        res = []
        for query in queries:
            res.append(pref[query[1] + 1] ^ pref[query[0]])
        return res