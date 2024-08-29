class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = str(num)
            num = sum([int(i) for i in num])
        return num