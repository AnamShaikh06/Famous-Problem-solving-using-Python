class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n=len(arr)
        arr[d%n:],arr[:d%n]=arr[:d%n],arr[d%n:]
        return arr
s=Solution()
print(s.rotateArr([10,20,30,40,50],6))