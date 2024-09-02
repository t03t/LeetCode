class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Sliding window:
        l, z = 0, 0
        m = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            while z > 0:
                if nums[l] == 0:
                    z -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
        
        