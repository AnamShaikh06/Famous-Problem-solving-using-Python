#Search the key in an array and return the index
class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
    
s=Solution()
print(s.search([10,20,30,40,50,60],40))