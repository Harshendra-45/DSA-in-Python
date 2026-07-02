class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        for i in nums:
            d[i]=nums.count(i)
        for k,v in d.items():
            if v==1:
                res.append(k)

        return res
