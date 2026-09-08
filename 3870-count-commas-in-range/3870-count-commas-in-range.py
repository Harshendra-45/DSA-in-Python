class Solution(object):
    def countCommas(self, n):
        if len(str(n))<=3:
            return 0
        else:
            c = 0
            for i in range(1000,n+1):
                c+=1
                temp = str(i)
                temp = temp[3:]
                if len(temp)>3:
                    c+=len(temp)//3
            return c