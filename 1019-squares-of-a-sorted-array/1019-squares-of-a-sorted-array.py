class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res, p = [0] * len(nums), len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[p] = nums[l] ** 2
                l += 1
            else:
                res[p] = nums[r] ** 2
                r -= 1
            p -= 1
        return res
