class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        flag=False
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j]!=needle[j]:
                        break
                else:
                    flag==True
                    return i
                    break
            else:
                flag = False

        if flag==False:
            return -1
