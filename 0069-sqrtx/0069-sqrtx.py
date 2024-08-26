class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x//2
        mid = 1
        while l <= r:
            mid = l + (r - l) // 2
            res = mid * mid
            if res == x:
                return mid
            if res < x:
                l = mid + 1
            if res > x:
                r = mid - 1
        return r