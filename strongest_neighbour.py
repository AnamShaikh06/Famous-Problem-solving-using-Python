#You are given an array arr[] consisting of positive integers. Return the maximum of every adjacent pairs in the array.
class Solution:
    def maxAdj(self, arr):
        ans=[]
        for i in range(len(arr)):
            if i==len(arr)-1:
                return ans
            if arr[i]>=arr[i+1]:
                ans.append(arr[i])
            else:
                ans.append(arr[i+1])
        return ans
        
s=Solution()
print(s.maxAdj([1,2,6,4,2,3,4,7,9]))     
        