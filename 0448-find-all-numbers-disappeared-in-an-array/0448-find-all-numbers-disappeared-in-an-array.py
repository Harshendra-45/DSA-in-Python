class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i in num:
                pass
            else:
                res.append(i)
        return res
        


        