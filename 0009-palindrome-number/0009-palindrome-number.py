class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = str(x)
        if m[::]==m[::-1]:
            return True
        else:
            return False