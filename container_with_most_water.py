#to identify a best length and height of the tank to hold more water in it
from typing import List
class Solution:
    def maxArea(self, ht: List[int]) -> int:
        ans=0
        l=0
        r=len(ht)-1
        
        while(l<r):
            height=min(ht[l],ht[r])
            width=r-l
            ans=max(height*width,ans)
            if ht[l]<ht[r]:
                l+=1
            else:
                r-=1
        return ans
s=Solution()
print(s.maxArea([1,2,3,5,8,6,4,5,9]))