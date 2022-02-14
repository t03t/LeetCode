class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        common1 = set(arr1).intersection(set(arr2))
        return sorted(common1.intersection(set(arr3)))