class Solution:
    def hammingWeight(self, n: int) -> int:
        two_power = int(math.log(n, 2))
        hamming = 0
        while (n > 0 and two_power >= 0):
            print("N: ", n)
            print("power: ", 2**two_power)
            if (n >= 2**two_power):
                hamming += 1
                n -= 2**two_power
            two_power -= 1
            print("hamming: ", hamming)
        return hamming
        if n == 0:
            return 0