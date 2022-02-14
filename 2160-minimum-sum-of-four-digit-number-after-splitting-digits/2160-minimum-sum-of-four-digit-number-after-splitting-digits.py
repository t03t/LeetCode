class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(n) for n in list(str(num))]
        
        mins = []
        mins.append(min(digits))
        digits.remove(min(digits))
        mins.append(min(digits))
        digits.remove(min(digits))
        mins[0]*= 10
        mins[0] += min(digits)
        digits.remove(min(digits))
        mins[1]*=10
        mins[1]+= min(digits)
        
        return mins[0]+mins[1]
        