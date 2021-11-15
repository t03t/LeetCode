class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = n
        ans = []
        for a, b in zip(nums[:mid], nums[mid:]):
            ans.append(a)
            ans.append(b)
        return ans