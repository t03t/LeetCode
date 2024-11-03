class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_counts = set()
        for num in nums:
            if num not in hash_counts and num > 0:
                hash_counts.add(num)
        for i in range(1, len(hash_counts)+1):
            if i not in hash_counts:
                return i
        return len(hash_counts)+1
