class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res=[]
        for i in bulbs:
            if i not in res and bulbs.count(i)%2!=0:
                res.append(i)
            
        return sorted(res)

        