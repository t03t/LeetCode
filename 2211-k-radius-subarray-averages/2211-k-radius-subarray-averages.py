class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        # sliding window + prefix_sum
        
        # find prefix_sum
        prefix_sum = [nums[0]]
        for num in nums[1:]:
            prefix_sum.append(num + prefix_sum[-1])
        
        # sliding_window
        res = [-1] * len(nums)
        window_size = 2 * k + 1
        if window_size > len(nums):
            return res
        for i in range(k, len(nums) - k):
            subSum = prefix_sum[i + k] - (prefix_sum[i - k - 1] if i - k - 1 >= 0 else 0)
            avg = subSum // window_size
            res[i] = avg
        return res