class Solution(object):
    def maxProduct(self, n):
        t = list((str(n)))
        t.sort(reverse=True)
        return int(t[0])*int(t[1])
        