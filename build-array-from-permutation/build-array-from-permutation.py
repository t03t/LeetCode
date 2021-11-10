class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        fake = nums
        for i in range(len(fake)):
            ans.append(fake[fake[i]])
        return ans
            