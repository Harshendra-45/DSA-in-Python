class Solution(object):
    def longestCommonPrefix(self, strs):
        m=strs[0]
        pr = strs[0]
        for i in strs:
            if len(i)<len(m):
                m = i

        strs.remove(m)
        for i in strs:
            temp=""
            for j in range(len(m)):
                if i[j]==m[j]:
                    temp+=i[j]
                else:
                    break
            if len(temp)<=len(pr) :
                pr = temp
        return pr