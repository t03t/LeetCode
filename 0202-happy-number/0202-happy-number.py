class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n!=1 and n not in cache:
            cache.add(n)
            n = sum(int(dig) ** 2 for dig in str(n))
        return n==1