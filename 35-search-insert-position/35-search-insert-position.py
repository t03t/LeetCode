class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        def searchBinary(nums: List[int], target: int, upper: int, lower: int):
            mid = (upper + lower)//2
            if nums[mid]==target:
                return mid
            elif lower==upper:
                if target>nums[mid]:
                    return mid+1
                return mid
            elif target<nums[mid]:
                upper = mid
                return searchBinary(nums, target, upper, lower)
            else:
                lower = mid+1
                return searchBinary(nums, target, upper, lower)
        return searchBinary(nums, target, len(nums)-1, 0)