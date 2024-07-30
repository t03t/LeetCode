class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map to store frequencies O(N)
        freq = Counter()
        for num in nums:
            freq[num] += 1
        # return k most frequent O(n log n)
        return (sorted(freq, key = freq.get, reverse = True)[0:k])
        
         