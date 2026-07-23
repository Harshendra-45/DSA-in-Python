class Solution(object):
    def topKFrequent(self, nums, k):
        y = dict()
        for i in nums:
            if i in y:
                y[i]+=1
            else: 
                y[i]=1
        ans=[]
        c = []
        for j,v in y.items():
            c.append(v)
        c.sort(reverse=True)
        c=c[:k]
        for j,v in y.items():
            if v in c:
                ans.append(j)
        return ans

    