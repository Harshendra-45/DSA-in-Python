class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = str(bin(n)[2:])
        return d.count('1')
