class Solution:
    def isHappy(self, n: int) -> bool:
        org = n
        n = abs(n)
        cache = {}
        while n:
            if n in cache:
                return cache[n] == 1
            sum_of_squares = 0
            for dig in list(str(n)):
                sum_of_squares += int(dig)**2
            cache[n] = sum_of_squares
            if sum_of_squares == 1:
                cache[org] = True
                return True
            n = sum_of_squares