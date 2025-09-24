class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]      # 1
        curr_sum = nums[0]     # 1
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])#max(-2,1-2)=-1,max(-2,-1-2)=-2,...
            max_sum = max(max_sum, curr_sum)#max(1,-1)=1,max(1,-2)=1,...
        
        return max_sum
s=Solution()
print(s.maxSubArray([1,-2,6,1,-8,5,3]))