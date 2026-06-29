class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        res= 0
        for i in nums:
            if i==1:
                c+=1
                # print(c)
            else:
                if c>res:
                    res=c
                c = 0
        if c>res:
            res=c
        return res

        