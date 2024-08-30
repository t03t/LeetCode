class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Long Ass Solution
        substr = ""
        for letter in s:
            substr += letter
            # check if repeat substring makes s
            if substr * (len(s)//len(substr)) == s and substr != s:
                return True
        return False

        #short one:
        # return s in (s + s)[1:-1]