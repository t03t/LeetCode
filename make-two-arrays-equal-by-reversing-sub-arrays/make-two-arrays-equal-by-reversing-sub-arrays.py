class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        for num in target:
            if counts[num]==0:
                return False
            counts[num] -= 1
        return True