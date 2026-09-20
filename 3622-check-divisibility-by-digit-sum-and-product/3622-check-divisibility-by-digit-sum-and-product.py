class Solution(object):
    def checkDivisibility(self, n):
        flag = False
        dsum=0
        dmul=1
        for i in str(n):
            dsum+=int(i)
            dmul*=int(i)
        s = dsum+dmul
        if n%s==0:
            flag=True
        return flag