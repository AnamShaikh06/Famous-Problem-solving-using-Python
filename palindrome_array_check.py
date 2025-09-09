# Palindrome if its reverse array matches the original array. 
from typing import List
class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        c=arr.copy()
        c.reverse()
        if c==arr:
            return True
        return False
            
s=Solution()
print(s.isPerfect([1,2,3,2,1]))
