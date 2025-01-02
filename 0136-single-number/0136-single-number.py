class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seenbefore=set()
        for num in nums:
            if num not in seenbefore:
                seenbefore.add(num)
            elif num in seenbefore:
                seenbefore.remove(num)
        return list(seenbefore)[0]