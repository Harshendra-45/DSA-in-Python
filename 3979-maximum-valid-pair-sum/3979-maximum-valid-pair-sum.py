class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans = 0
        best = nums[0]
        for j in range(k, len(nums)):
                best = max(best,nums[j-k])
                ans = max(ans,best+nums[j])
        return ans
