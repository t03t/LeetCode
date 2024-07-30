class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        longest = 1
        left = 0
        nums = sorted(set(nums))
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                left = i
            else:
                if i - left + 1 > longest:
                    longest = i - left + 1
        return longest
