class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum_values = ''
        for letter in s:
            sum_values += str(ord(letter)%96)
        i = 0
        while i < k:
            values = list(int(digit) for digit in str(sum_values))
            sum_values = sum(values)
            i += 1
        return sum_values