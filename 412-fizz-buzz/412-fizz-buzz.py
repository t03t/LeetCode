class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            fb = ""
            if i%3 == 0:
                fb+="Fizz"
            if i%5 == 0:
                fb+= "Buzz"
            if len(fb)==0:
                ans.append(str(i))
            else:
                ans.append(fb)
        return ans