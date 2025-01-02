class Solution:
    def maxScore(self, s: str) -> int:
        l, r = 0, 0
        prefix_sum = [0 for _ in range(len(s))]
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            prefix_sum[i] = int(s[i]) + prev
            prev = prefix_sum[i]
        print(prefix_sum)
        l, r = 0, 0
        res = 0
        for i in range(len(s) - 1):
            cur = (1 if int(s[i]) == 0 else 0)
            l += cur
            r = prefix_sum[i+1]
            res = max(res, l + r)
        return res

