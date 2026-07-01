class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fr= 0
        d = len(nums)-1

        
        for i in range(len(nums)):
            if i>fr:
             return False
            temp = nums[i]
            fr = max(fr, i + nums[i])
        if fr>=d:
            return True
        

        