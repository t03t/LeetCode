class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i, elem in enumerate(nums1):
            found_in_nums2 = False
            for j, elem2 in enumerate(nums2):
                if found_in_nums2 and elem2 > elem:
                    res[i] = elem2
                    break
                if elem2 == elem:
                    found_in_nums2 = True
        return res