class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if i==0 and nums[i]>target:
                    k = i
                    break
            elif nums[i]==target:
                k = i
                break
            else:
                if len(nums)==1 and nums[i]<target:
                    k = i+1
                    break
                elif i==len(nums)-1 and nums[i]<target:
                    k=i+1
                    break
                elif nums[i]<target:
                    pass
                else:
                    k=i
                    break
                
        return k