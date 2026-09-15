class Solution(object):
    def runningSum(self, nums):
        arr=[]
        for i in range(len(nums)):
            if i==0:
                arr.append(nums[i])
            else:

                arr.append(nums[i]+arr[i-1])
        return arr
        