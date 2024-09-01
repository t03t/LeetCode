class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= 1:
            return sum(nums)
        l, r = 0, k-1
        sum_ = sum(nums[l:r+1])
        max_sum = sum_
        while r < len(nums) -  1:
            print(l, r, sum_, max_sum)
            if sum_ > max_sum :
                max_sum = sum_
            sum_ -= nums[l]
            l += 1
            r += 1
            sum_ += nums[r]
        if sum_ > max_sum :
            max_sum = sum_
        return max_sum/k
            
            
            
        