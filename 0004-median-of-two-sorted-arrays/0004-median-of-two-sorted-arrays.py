class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
    
        c = len(nums1)+len(nums2)
        nums1.extend(nums2)
        z = sorted(nums1)
        if c%2!=0:
            a=(c)//2
            p = z[a]
            return p
        else:
            a=(z[c//2])
            b=(z[(c//2)-1])
            d = a+b
            e = d/2
            print(e)
            return e