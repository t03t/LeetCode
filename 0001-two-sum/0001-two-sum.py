class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - nums[i]
            if complement in dic:
                return [i, dic[complement]]
            dic[num] = i
        return [-1, -1]