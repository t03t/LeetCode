class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i,n in enumerate(nums):
            if i%2==0:
                freq = n
            if i%2==1:
                if freq:
                    decompress.extend([n for i in range(freq)])
        return decompress