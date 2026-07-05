class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)//2
        if nums.count(nums[n])==1:
            return True
        else:
            return False
        