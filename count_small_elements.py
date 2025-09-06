#count the elements which are less or equal to y in the array

class Solution:
    def countOfElements(self, x, arr):
        c=0
        for i in range(len(arr)):
            if arr[i]<=x:
                c+=1
        return c
s=Solution()
print(s.countOfElements(10,[10,9,7,8,12,60,10,10.0,10.000,1]))   
