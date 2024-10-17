class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter()
        for num in nums:
            freq[num] += 1
        largest = -1
        for _ in freq.keys():
            if freq[_] == 1:
                if _ > largest:
                    largest = _
        return largest