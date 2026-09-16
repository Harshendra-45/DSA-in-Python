class Solution(object):
    def findLucky(self, arr):
        n = -1
        m = []
        for i in arr:
            if arr.count(i)==i:
               m.append(i)
        if m!=[]:
            return max(m)
        else:
            return -1
        