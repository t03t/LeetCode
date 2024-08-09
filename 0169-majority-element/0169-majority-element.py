from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter()
        majority = len(nums)//2
        for num in nums:
            counts[num] += 1
            if counts[num] > majority:
                return num
        return -1