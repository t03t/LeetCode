class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # get prefix sum
        res = 0
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        for i in range(len(nums) - 1):
            left = prefix_sum[i]
            right = prefix_sum[-1] - prefix_sum[i]
            if left >= right:
                res += 1
        return res
