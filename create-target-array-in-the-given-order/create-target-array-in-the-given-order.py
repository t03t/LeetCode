class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, dig in enumerate(index):
            target.insert(dig, nums[i])
        return target