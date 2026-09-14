class Solution(object):
    def alternateDigitSum(self, n):
        n = str(n)
        s = 0
        for i in  range(len(n)):
            if i==0 or i%2==0:
                s+=int(n[i])
            else:
                s-=int(n[i])
        return s