class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        largest_outlier = float('-inf')
        num_counts = Counter(nums)
        for i in range(len(nums)):
            sum_without_potential_outlier = total - nums[i]
            num_counts[nums[i]] -= 1
            if num_counts[sum_without_potential_outlier/2] >= 1:
                if nums[i] > largest_outlier:
                    largest_outlier = nums[i]
            num_counts[nums[i]] += 1
        return largest_outlier