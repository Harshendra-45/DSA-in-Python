class Solution(object):
    def maximumWealth(self, accounts):
        m=0
        for i in accounts:
            temp = i
            s=0
            for j in temp:
                s+=j
                if s>m:
                    m=s
        return m

        