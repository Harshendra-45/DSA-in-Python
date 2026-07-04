class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            if nums.count(i)==1:
                ans+=i
        return ans
