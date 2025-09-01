#Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
class Solution:
    def search(self, arr, x):
        # code here
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
    
s=Solution()
print(s.search([10,20,50,60,90,25,90,27,63,101],90))