class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        summation = 0
        for num1,num2 in zip(sorted(nums1),sorted(nums2, reverse=True)):
            summation += num1*num2
        return summation