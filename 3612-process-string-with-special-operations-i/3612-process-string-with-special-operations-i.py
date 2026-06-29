class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in s:
            if i=='*':
                res = res[:-1]
            elif i =='#':
                res +=res
            elif i=='%':
                res = res[::-1]
            else:
                res+=i
        return res
        