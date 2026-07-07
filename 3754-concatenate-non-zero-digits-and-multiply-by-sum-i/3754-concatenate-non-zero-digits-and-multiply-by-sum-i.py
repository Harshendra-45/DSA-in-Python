class Solution:
    def sumAndMultiply(self, n: int) -> int:
        st1 = str(n)
        sums = 0
        res=""
        for i in st1:
            if i!='0':
                res+=i
                sums+=int(i)
        if res=="":
            return 0
        else:
             return int(res)*sums

