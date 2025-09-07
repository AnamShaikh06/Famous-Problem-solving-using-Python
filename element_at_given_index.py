#display element at given index
from typing import List
class Solution:
    def findElementAtIndex(self, key : int, arr : List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if i==key:
                return arr[i]
s=Solution()
print(s.findElementAtIndex(3,[1,2,6,7,8,3,2,1]))