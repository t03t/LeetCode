class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        code= {"6":"9", "8":"8", "9":"6", "0":"0", "1":"1"}
        code180 = {"0":"0", "1":"1", "8":"8"}
        if (len(num)==1):
            if num in ["0", "1", "8"]:
                return True
            return False
        reverse = ""
        for i in range(len(num)-1,-1,-1):
            if num[i] not in code:
                return False
            else:
                reverse += code[num[i]]
        if reverse == num:
            return True
        return False