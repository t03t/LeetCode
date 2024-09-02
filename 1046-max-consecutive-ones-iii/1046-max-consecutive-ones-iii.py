class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Given a binary array nums and an integer k, return the maximum number of consecutive 1's in           # the array if you can flip at most k 0's.
        
        # Sliding Window Approach
        l, z = 0, 0
        max_consec = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            
            max_consec = max(max_consec, r - l + 1)
        return max_consec
            
            
            