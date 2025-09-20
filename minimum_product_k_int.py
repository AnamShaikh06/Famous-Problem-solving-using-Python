#to find the minimum product of k integers given by user
#only consider k elements and find those element which will give minimum product.
class Solution:
    def minProduct(self, arr, k): 
        arr.sort()
        p=1
        for i in range(k):
            if i==len(arr):
                return (p%((10**9)+7))
            p*=arr[i]
        return (p%((10**9)+7))
            
s=Solution()
print(s.minProduct([2,5,6,7,2,5],3))