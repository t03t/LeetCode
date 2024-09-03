class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from the left
        # swap the nonZero with a zero on the left and let it trickle
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0: # If r is non zero, replace it with previous zero
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                # zeros will trickle down to the end
        