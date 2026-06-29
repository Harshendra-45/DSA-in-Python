class Solution(object):
    def twoSum(self, nums, target):
        
        hashmap = {}

        for i in range(len(nums)):

            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]

            else:
                hashmap[nums[i]] = i