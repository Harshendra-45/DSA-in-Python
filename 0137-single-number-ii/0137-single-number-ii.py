class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            d[i]=nums.count(i)
        # print(d)
        for k,v in d.items():
            if v==1:
                return k
                break
