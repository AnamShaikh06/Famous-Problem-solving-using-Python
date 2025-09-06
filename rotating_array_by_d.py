#Rotating an array by d elements 
class Solution:
    def leftRotate(self, arr, d):
       
        arr[:]=arr[d:]+arr[0:d]
        return arr
    
s=Solution()
print(s.leftRotate([10,20,30,-4,9,6],2))