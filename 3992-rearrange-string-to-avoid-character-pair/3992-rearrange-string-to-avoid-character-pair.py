class Solution(object):
    def rearrangeString(self, s, x, y):
        res=""
        temp=""
        for i in s:
            if i!=x:
                res+=i
            else:
                temp+=i
        res+=temp
        return res
        