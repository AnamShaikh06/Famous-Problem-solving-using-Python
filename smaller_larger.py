#Given a sorted array arr and a value target, return an array of size 2. The first value is the number of elements less than or equal to the target, and the second value is the number of elements greater than or equal to the target.
class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        s=0
        l=0
        for i in range(len(arr)):
            if arr[i]<=target:
                s+=1
            if arr[i]>=target:
                l+=1
        
        return s,l
s=Solution()
print(s.getMoreAndLess([1,2,5,6,4,7,8,9],4))		        