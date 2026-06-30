class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                ans += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return ans