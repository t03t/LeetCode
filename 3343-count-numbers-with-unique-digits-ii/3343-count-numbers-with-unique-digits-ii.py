class Solution:
    def numberCount(self, a: int, b: int) -> int:
        uniques = 0
        for i in range(a, b + 1):
            if len(str(i)) == len(set(list(str(i)))):
                uniques += 1
        return uniques