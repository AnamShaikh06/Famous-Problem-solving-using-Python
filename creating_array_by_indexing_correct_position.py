from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.insert(index[i],nums[i])
        return ans
s=Solution()
print(s.createTargetArray([0,1,2,3,4],[0,1,2,2,1]))