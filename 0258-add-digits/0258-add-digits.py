class Solution:
    def addDigits(self, num: int) -> int:
        addition = str(num)
        while len(addition) != 1:
            add_sum = 0
            for digit in addition:
                add_sum += int(digit)
            addition = str(add_sum)
        return int(addition)