class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        max_right_stack = [0] * n
        max_right = nums[-1]
        max_right_stack[-1] = max_right

        for r in range(n - 2, -1, -1):
            max_right = max(max_right, nums[r])
            max_right_stack[r] = max_right

        max_width = 0
        l = 0
        for r in range(n):
            while l < r and nums[l] > max_right_stack[r]:
                l += 1
            max_width = max(max_width, r - l)
        
        return max_width