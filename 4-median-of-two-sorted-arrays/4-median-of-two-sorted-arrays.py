class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1+nums2)
        length = len(combined)
        if length%2 != 0:
            return combined[(length//2)]
        else:
            med1 = combined[(length//2)-1]
            med2 = combined[(length//2)]
            return (med1+med2)/2