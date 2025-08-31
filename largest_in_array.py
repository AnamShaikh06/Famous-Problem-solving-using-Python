#To find the largest element in the array 

class Solution:
    def largest(self, arr):
        # code here
        ans=arr[0]
        for i in range(len(arr)):
            if ans<arr[i]:
                ans=arr[i]
            
        return ans
    
s=Solution()
print(s.largest([10,20,50,60,90,25,27,63,101]))