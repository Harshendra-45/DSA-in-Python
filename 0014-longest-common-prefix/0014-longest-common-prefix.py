class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Find the shortest string
        m = min(strs, key=len)

        prefix = ""

        # Check each character position of the shortest string
        for j in range(len(m)):
            for s in strs:
                if s[j] != m[j]:
                    return prefix
            prefix += m[j]

        return prefix