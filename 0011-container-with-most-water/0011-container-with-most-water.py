class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1

        ans = 0

        while left < right:

            area = min(height[left], height[right])*(right-left)
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans