class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = (len(arr)/4)+1
        
        for i in arr:
            if arr.count(i)>=n:
                return i
                break