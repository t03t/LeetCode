class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Sliding window:
        c = m = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                m = max(m, c)
                c = 0
        return max(m, c)