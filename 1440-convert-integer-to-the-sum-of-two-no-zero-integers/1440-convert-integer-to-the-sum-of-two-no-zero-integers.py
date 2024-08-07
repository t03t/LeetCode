class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def nonZero(c: int):
            return "0" not in list(str(c))
        a = 1
        for i in range(n-1, 0, -1):
            if nonZero(i) and nonZero(a):
                return [a, i]
            else:
                a += 1
        return []