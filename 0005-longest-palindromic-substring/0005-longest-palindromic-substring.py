class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longest_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > longest_len:
                    longest = s[l:r+1]
                    longest_len = r-l+1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > longest_len:
                    longest = s[l:r+1]
                    longest_len = r-l+1
                l -= 1
                r += 1
            
        return longest

        # Brute Force O(N^2) * O(N) for palindrome check
        # def isPalindrome(s: str):
        #     if len(s) % 2 == 0:
        #         return (s[0:len(s)//2] == s[len(s)//2:][::-1])
        #     return (s[0:len(s)//2] == s[len(s)//2+1:][::-1])
        # if len(s) <= 1:
        #     return s
        # longest = None
        # for i in range(len(s)): # e.g. 0 - 5
        #     for j in range(i + 1, len(s)): # 1 - 5
        #         if isPalindrome(s[i:j]): # [0:1], [0:2]etc
        #             if not longest:
        #                 longest = s[i:j]
        #             if (len(s[i:j]) > len(longest)):
        #                 longest = s[i:j]
        # return longest

        