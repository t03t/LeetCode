class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        count = 0
        cum_counts = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in cum_counts:
                res = max(res, i - cum_counts[count])
            else:
                cum_counts[count] = i
        return res