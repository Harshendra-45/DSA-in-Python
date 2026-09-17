class Solution(object):
    def numberOfSteps(self, num):
        temp = num
        step=0
        for i in range(num):
            if temp==0:
                break
            if temp%2==0:
                temp/=2
                step+=1
            else:
                temp-=1
                step+=1
        return step