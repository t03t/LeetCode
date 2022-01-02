class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(str(n))
        summ = 0
        product = 1
        for digit in digits:
            d = int(digit)
            summ += d
            product *= d
        return product - summ