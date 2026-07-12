class Solution(object):
    def checkGoodInteger(self, n):
        
        s = 0
        sq=0
        for i in str(n):
            s+=int(i)
            sq+=int(i)**2
        return sq-s>=50
            
        
