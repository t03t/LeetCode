class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        map = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "Z": 0}
        
        # XCIV = 1 5
        prev = "Z"
        for i in range(len(s)-1, -1, -1):
            cur = s[i]
            print("Cur:", cur, "Prev: ", prev)
            if map[cur] < map[prev]:
                number -= map[cur]
            else:
                number += map[cur]
                prev = cur 
        return number