class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([int(n) for n in list(str(num))])
        mins = [(digits[0]*10)+digits[2],(digits[1]*10)+digits[3]]
        return mins[0]+mins[1]
        