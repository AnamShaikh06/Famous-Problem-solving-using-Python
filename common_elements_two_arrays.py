#count of common elements in both
from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=c2=0
        for i in nums1:
            if i in nums2:
                c1+=1
        for i in nums2:
            if i in nums1:
                c2+=1
        return [c1]+[c2]
s=Solution()
print(s.findIntersectionValues([2,3,2],[1,2]))