class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        else:
            for i in range(len(nums)):
                if i==0:
                    if nums[i]>nums[i+1]:
                        return i
                elif i==len(nums)-1:
                    if nums[i]>nums[i-1]:
                        return i
                elif nums[i-1]<nums[i]>nums[i+1]:
                    return i
                
