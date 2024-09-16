class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(t: str) -> int:
            h, m = map(int, t.split(":"))
            return h * 60 + m
        
        minutes = sorted([timeToMinutes(tp) for tp in timePoints])
        
        minD = float('inf')
        
        for i in range(1, len(minutes)):
            minD = min(minD, minutes[i] - minutes[i - 1])
        
        return min(minD, 1440 - (minutes[-1] - minutes[0]))