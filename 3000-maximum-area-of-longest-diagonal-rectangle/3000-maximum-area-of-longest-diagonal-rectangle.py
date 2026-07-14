class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dl=0
        area=0
        for i in dimensions:
            print(i)
            temp=(i[0]**2)+(i[1]**2)
            print(temp)
            if temp==dl:
                dl=temp
                area1 = i[0]*i[1]
                if area1>area:
                    area=area1
            elif temp>dl:
                dl=temp
                area=i[0]*i[1]
        return area
            

        