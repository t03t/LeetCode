class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while len(nums) != len(set(nums)) and len(nums) > 3:
            nums = nums[3:]
            res+=1
        if len(nums) != len(set(nums)):
            res += 1
        return res
