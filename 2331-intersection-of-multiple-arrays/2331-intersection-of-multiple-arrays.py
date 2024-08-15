class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set()
        for arr in nums:
            if not common:
                common.update(arr)
            else:
                common = common.intersection(arr)
        return sorted(common)