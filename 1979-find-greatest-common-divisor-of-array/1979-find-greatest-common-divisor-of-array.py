class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        n = min(nums)
        gcd=1
        for i in range(1,m+1):
            if m%i==0 and n%i==0:
                gcd=i
        return gcd
        