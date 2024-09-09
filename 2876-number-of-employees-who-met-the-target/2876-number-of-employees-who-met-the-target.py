class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for h in hours:
            res += 1 if h >= target else 0
        return res