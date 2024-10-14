class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # It is not required to do the modifications in-place.
        pos, neg = [], []
        for num in nums:
            if num >= 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
        return res