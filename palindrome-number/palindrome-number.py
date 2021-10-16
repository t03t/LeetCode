class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        forward = str(x)
        backwards = forward[::-1]
        return forward == backwards
        