class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in nums]
        for i, A in enumerate(nums):
            for j, B in enumerate(nums):
                if i!=j:
                    if B<A:
                        ans[i]+=1
        return ans
                    