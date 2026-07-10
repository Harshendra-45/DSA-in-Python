class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fl = False
        for i in nums:
            print(fl)
            t=nums.count(i)
            print(i)
            print(t)
            if t==1:
                fl= False
            else:
                for j in range(2,int(t**0.5)+1):
                    print(j)
                    if t%j==0:
                        fl=False
                        print(fl)
                        break
                else:
                    fl = True
                    break
        return fl