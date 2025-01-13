class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        def get_trio(n):
            res = []
            h = n // 100
            if h:
                res.append(ones[h] + " Hundred")
            t = n % 100
            if t >= 20:
                t_tens, t_ones = t // 10, t % 10
                res.append(tens[t_tens])
                if t_ones:
                    res.append(ones[t_ones])
            elif t:
                res.append(ones[t])
            return " ".join(res)       
        res = []
        place_value = ["", "Thousand", "Million", "Billion"]
        i = 0
        while num:
            trio_dig = num % 1000
            s = get_trio(trio_dig)
            num = num // 1000
            if s:
                res.append(s + " " + place_value[i])
            i += 1
        
        return " ".join(reversed(res)).strip()