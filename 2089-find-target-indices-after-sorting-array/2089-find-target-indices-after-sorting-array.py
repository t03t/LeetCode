class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        ind = []
        for i,n in enumerate(nums):
            if n == target:
                ind.append(i)
        return ind