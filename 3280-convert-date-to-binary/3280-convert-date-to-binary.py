class Solution(object):
    def convertDateToBinary(self, date):
        dat = date.split("-")
        ans=""
        for i in dat:
            ans+="-"
            i = int(i)   
            print(i) 
            ans+=str(bin(i))[2:]
        return ans[1:]

        