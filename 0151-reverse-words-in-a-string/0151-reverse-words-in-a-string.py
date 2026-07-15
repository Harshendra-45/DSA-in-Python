class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s.split()
        p=t[::-1]
        res=" ".join(p)
        return res