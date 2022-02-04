class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(3):
            for j in range(len(nums)):
                if nums[j]==i:
                    nums[count],nums[j] = nums[j],nums[count]
                    count += 1
        