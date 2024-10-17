class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        counts[0] = 1
        ans = curr = 0
        for num in nums:
            curr += num
            ans += counts[curr-k]
            counts[curr] += 1
        return ans