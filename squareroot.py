import math
class Solution:
    def floorSqrt(self, n): 
        # code here
        return math.floor(n**0.5)
s=Solution()  
print(s.floorSqrt(10))
print(s.floorSqrt(36))
