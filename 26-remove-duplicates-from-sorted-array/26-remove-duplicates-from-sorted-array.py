class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0
        for i, num in enumerate(nums):
            if prev!=None:
                if prev == num:
                    nums[i-1]="_"
                    k+=1
            prev = num
        #must push all of the _'s towards the back
        pointer = 0
        for j, num in enumerate(nums):
            if num!= "_":
                nums[pointer] = num
                pointer+=1
        return len(nums)-k