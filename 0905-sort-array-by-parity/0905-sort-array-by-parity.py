class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans =[]
        for i in nums[:]:
            if i%2==0:
                ans.append(i)
                nums.remove(i)
        ans.extend(nums)
        return ans