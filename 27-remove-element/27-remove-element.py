class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i]="_"
                k+=1
        #must push all of the _'s towards the back
        pointer = 0
        for j, num in enumerate(nums):
            if num!= "_":
                nums[pointer] = num
                pointer+=1
        return len(nums)-k