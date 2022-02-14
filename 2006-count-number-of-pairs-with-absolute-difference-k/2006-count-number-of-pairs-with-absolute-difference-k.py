class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        seenbefore = set()
        for i,num in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i != j and (i,j) not in seenbefore and (j, i) not in seenbefore:
                    if abs(num-num2)==k:
                        count+=1
                        seenbefore.add((i,j))
        return count